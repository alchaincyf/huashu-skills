#!/usr/bin/env python3
"""
蜂群观测台 - Swarm Dashboard
用法: python3 dashboard.py [项目目录] [端口]
示例: python3 dashboard.py /path/to/project 8420
"""

import http.server
import json
import os
import subprocess
import sys
import urllib.parse
from pathlib import Path

PROJECT_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8420
PROJECT_NAME = PROJECT_DIR.name
SESSION_NAME = f"swarm-{PROJECT_NAME}"


def run_cmd(cmd, cwd=None):
    """运行shell命令，返回输出"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            cwd=cwd or str(PROJECT_DIR), timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return f"error: {e}"


def get_status():
    """获取蜂群完整状态"""
    # tmux状态
    tmux_running = run_cmd(f"tmux has-session -t {SESSION_NAME} 2>/dev/null && echo 'yes' || echo 'no'")
    pane_count = 0
    if tmux_running == "yes":
        pane_count = int(run_cmd(f"tmux list-panes -t {SESSION_NAME} 2>/dev/null | wc -l").strip() or "0")

    # git log
    git_log = run_cmd("git log --oneline --all -30")

    # TASKS.md
    tasks_file = PROJECT_DIR / "TASKS.md"
    tasks_content = tasks_file.read_text() if tasks_file.exists() else ""

    # 统计任务
    task_total = tasks_content.count("- [")
    task_done = tasks_content.count("- [x]")
    task_in_progress = tasks_content.count("- [~]")
    task_todo = task_total - task_done - task_in_progress

    # lock文件
    locks = []
    lock_dir = PROJECT_DIR / "current_tasks"
    if lock_dir.exists():
        for f in lock_dir.glob("*.lock"):
            locks.append({
                "task": f.stem,
                "owner": f.read_text().strip()
            })

    # worktree状态
    worktrees = []
    for d in sorted(PROJECT_DIR.parent.glob(f"{PROJECT_NAME}-agent-*")):
        if d.is_dir():
            agent_num = d.name.split("-")[-1]
            last_commit = run_cmd("git log --oneline -1", cwd=str(d))
            worktrees.append({
                "id": agent_num,
                "dir": str(d),
                "last_commit": last_commit
            })

    # 最近日志
    log_dir = PROJECT_DIR / "agent_logs"
    recent_logs = []
    if log_dir.exists():
        log_files = sorted(log_dir.glob("*.log"), key=lambda f: f.stat().st_mtime, reverse=True)
        for lf in log_files[:8]:
            try:
                lines = lf.read_text().splitlines()
                tail = lines[-15:] if len(lines) > 15 else lines
                recent_logs.append({
                    "file": lf.name,
                    "tail": "\n".join(tail),
                    "size": lf.stat().st_size,
                    "mtime": lf.stat().st_mtime
                })
            except:
                pass

    # HUMAN_INPUT.md
    hi_file = PROJECT_DIR / "HUMAN_INPUT.md"
    human_input = hi_file.read_text().strip() if hi_file.exists() else ""

    return {
        "project": PROJECT_NAME,
        "project_dir": str(PROJECT_DIR),
        "tmux_running": tmux_running == "yes",
        "pane_count": pane_count,
        "git_log": git_log,
        "tasks_content": tasks_content,
        "task_stats": {
            "total": task_total,
            "done": task_done,
            "in_progress": task_in_progress,
            "todo": task_todo
        },
        "locks": locks,
        "worktrees": worktrees,
        "recent_logs": recent_logs,
        "human_input": human_input
    }


def send_human_input(message):
    """发送人类指令"""
    import datetime
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hi_file = PROJECT_DIR / "HUMAN_INPUT.md"
    hi_file.write_text(f"# 人类指令 - {ts}\n\n{message}\n")

    run_cmd("git add HUMAN_INPUT.md")
    run_cmd(f'git commit -m "HUMAN: {message[:50]}"')
    run_cmd("git push origin main 2>/dev/null || true")
    return {"ok": True, "message": message}


DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Swarm Dashboard</title>
<style>
  :root {
    --bg: #1a1a2e;
    --surface: #16213e;
    --surface2: #1a2744;
    --border: #2a3a5c;
    --text: #e0e0e0;
    --text2: #8892a4;
    --accent: #4ecca3;
    --accent2: #3ba386;
    --warn: #e8a838;
    --error: #e84855;
    --done: #4ecca3;
    --running: #38b6ff;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }

  /* Header */
  .header {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h1 {
    font-size: 18px;
    font-weight: 600;
    color: var(--accent);
  }
  .header h1 span { color: var(--text2); font-weight: 400; }
  .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 500;
  }
  .status-badge.running {
    background: rgba(78, 204, 163, 0.15);
    color: var(--accent);
  }
  .status-badge.stopped {
    background: rgba(232, 72, 85, 0.15);
    color: var(--error);
  }
  .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  .status-dot.running { background: var(--accent); animation: pulse 2s infinite; }
  .status-dot.stopped { background: var(--error); }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  /* Layout */
  .main {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto 1fr;
    gap: 16px;
    padding: 16px 24px;
    max-width: 1600px;
    margin: 0 auto;
  }

  /* Cards */
  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
  }
  .card-header {
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .card-header h2 {
    font-size: 13px;
    font-weight: 600;
    color: var(--text2);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .card-body { padding: 12px 16px; }

  /* Stats bar */
  .stats-bar {
    grid-column: 1 / -1;
    display: flex;
    gap: 16px;
  }
  .stat-card {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    text-align: center;
  }
  .stat-value {
    font-size: 28px;
    font-weight: 700;
    color: var(--accent);
  }
  .stat-value.warn { color: var(--warn); }
  .stat-value.running-color { color: var(--running); }
  .stat-label {
    font-size: 11px;
    color: var(--text2);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* Agent list */
  .agent-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(42, 58, 92, 0.5);
    font-size: 13px;
  }
  .agent-item:last-child { border-bottom: none; }
  .agent-id {
    background: var(--surface2);
    color: var(--running);
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    min-width: 28px;
    text-align: center;
  }
  .agent-commit {
    color: var(--text2);
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  /* Lock list */
  .lock-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 0;
    border-bottom: 1px solid rgba(42, 58, 92, 0.5);
    font-size: 13px;
  }
  .lock-task {
    color: var(--warn);
    font-weight: 500;
  }
  .lock-owner { color: var(--text2); }

  /* Tasks */
  .tasks-content {
    font-size: 13px;
    line-height: 1.6;
    white-space: pre-wrap;
    max-height: 300px;
    overflow-y: auto;
  }

  /* Git log */
  .git-log {
    font-size: 12px;
    line-height: 1.7;
    max-height: 300px;
    overflow-y: auto;
    color: var(--text2);
  }
  .git-log .hash {
    color: var(--warn);
  }

  /* Logs */
  .logs-area {
    grid-column: 1 / -1;
  }
  .log-tabs {
    display: flex;
    gap: 0;
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
  }
  .log-tab {
    padding: 8px 14px;
    font-size: 12px;
    color: var(--text2);
    cursor: pointer;
    border-bottom: 2px solid transparent;
    white-space: nowrap;
    background: none;
    border-top: none;
    border-left: none;
    border-right: none;
    font-family: inherit;
  }
  .log-tab:hover { color: var(--text); }
  .log-tab.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
  }
  .log-content {
    font-size: 12px;
    line-height: 1.6;
    padding: 12px 16px;
    max-height: 250px;
    overflow-y: auto;
    white-space: pre-wrap;
    color: var(--text2);
    background: rgba(0,0,0,0.2);
  }

  /* Input area */
  .input-area {
    grid-column: 1 / -1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
  }
  .input-area h2 {
    font-size: 13px;
    font-weight: 600;
    color: var(--text2);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
  }
  .input-row {
    display: flex;
    gap: 10px;
  }
  .input-row input {
    flex: 1;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 14px;
    color: var(--text);
    font-family: inherit;
    font-size: 14px;
    outline: none;
  }
  .input-row input:focus {
    border-color: var(--accent);
  }
  .input-row input::placeholder { color: var(--text2); }
  .btn {
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    font-family: inherit;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s;
  }
  .btn-send {
    background: var(--accent);
    color: var(--bg);
  }
  .btn-send:hover { background: var(--accent2); }
  .btn-send:disabled { opacity: 0.5; cursor: not-allowed; }
  .btn-stop {
    background: rgba(232, 72, 85, 0.15);
    color: var(--error);
    border: 1px solid var(--error);
  }
  .btn-stop:hover { background: rgba(232, 72, 85, 0.3); }
  .pending-input {
    margin-top: 8px;
    font-size: 12px;
    color: var(--warn);
  }
  .toast {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: var(--accent);
    color: var(--bg);
    padding: 10px 20px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s;
    pointer-events: none;
  }
  .toast.show {
    opacity: 1;
    transform: translateY(0);
  }
  .empty { color: var(--text2); font-size: 13px; font-style: italic; }
  .refresh-info {
    font-size: 11px;
    color: var(--text2);
  }

  /* scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
</style>
</head>
<body>

<div class="header">
  <h1>SWARM <span id="project-name"></span></h1>
  <div style="display:flex;align-items:center;gap:16px">
    <span class="refresh-info" id="refresh-info"></span>
    <span class="status-badge" id="tmux-badge">
      <span class="status-dot" id="tmux-dot"></span>
      <span id="tmux-text"></span>
    </span>
  </div>
</div>

<div class="main">
  <!-- Stats -->
  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-value running-color" id="stat-agents">-</div>
      <div class="stat-label">Agents</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="stat-done">-</div>
      <div class="stat-label">Done</div>
    </div>
    <div class="stat-card">
      <div class="stat-value warn" id="stat-progress">-</div>
      <div class="stat-label">In Progress</div>
    </div>
    <div class="stat-card">
      <div class="stat-value running-color" id="stat-todo">-</div>
      <div class="stat-label">Todo</div>
    </div>
  </div>

  <!-- Agents -->
  <div class="card">
    <div class="card-header"><h2>Agents</h2></div>
    <div class="card-body" id="agents-list">
      <span class="empty">loading...</span>
    </div>
  </div>

  <!-- Active Tasks (locks) -->
  <div class="card">
    <div class="card-header"><h2>Active Tasks</h2></div>
    <div class="card-body" id="locks-list">
      <span class="empty">loading...</span>
    </div>
  </div>

  <!-- TASKS.md -->
  <div class="card">
    <div class="card-header"><h2>Tasks.md</h2></div>
    <div class="card-body">
      <div class="tasks-content" id="tasks-content">loading...</div>
    </div>
  </div>

  <!-- Git Log -->
  <div class="card">
    <div class="card-header"><h2>Git Log</h2></div>
    <div class="card-body">
      <div class="git-log" id="git-log">loading...</div>
    </div>
  </div>

  <!-- Logs -->
  <div class="card logs-area">
    <div class="card-header"><h2>Agent Logs</h2></div>
    <div class="log-tabs" id="log-tabs"></div>
    <div class="log-content" id="log-content">选择一个agent日志查看</div>
  </div>

  <!-- Human Input -->
  <div class="input-area">
    <h2>Send Command to Agents</h2>
    <div class="input-row">
      <input type="text" id="human-input" placeholder="输入指令，agent下一个session会优先执行..."
             onkeydown="if(event.key==='Enter')sendInput()">
      <button class="btn btn-send" id="send-btn" onclick="sendInput()">发送</button>
      <button class="btn btn-stop" onclick="stopSwarm()">Stop All</button>
    </div>
    <div class="pending-input" id="pending-input"></div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
let currentLogIndex = 0;
let statusData = null;

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

function formatGitLog(log) {
  if (!log) return '<span class="empty">no commits</span>';
  return log.split('\\n').map(line => {
    const parts = line.match(/^([a-f0-9]+)\\s(.*)$/);
    if (parts) return `<span class="hash">${parts[1]}</span> ${escHtml(parts[2])}`;
    return escHtml(line);
  }).join('\\n');
}

function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

async function fetchStatus() {
  try {
    const res = await fetch('/api/status');
    statusData = await res.json();
    render(statusData);
  } catch(e) {
    console.error('fetch error:', e);
  }
}

function render(d) {
  document.getElementById('project-name').textContent = d.project;
  document.title = `Swarm - ${d.project}`;

  // tmux badge
  const badge = document.getElementById('tmux-badge');
  const dot = document.getElementById('tmux-dot');
  const txt = document.getElementById('tmux-text');
  if (d.tmux_running) {
    badge.className = 'status-badge running';
    dot.className = 'status-dot running';
    txt.textContent = `Running (${d.pane_count} panes)`;
  } else {
    badge.className = 'status-badge stopped';
    dot.className = 'status-dot stopped';
    txt.textContent = 'Stopped';
  }

  // refresh info
  document.getElementById('refresh-info').textContent =
    `Updated ${new Date().toLocaleTimeString()}`;

  // stats
  document.getElementById('stat-agents').textContent = d.worktrees.length;
  document.getElementById('stat-done').textContent = d.task_stats.done;
  document.getElementById('stat-progress').textContent = d.task_stats.in_progress;
  document.getElementById('stat-todo').textContent = d.task_stats.todo;

  // agents
  const al = document.getElementById('agents-list');
  if (d.worktrees.length === 0) {
    al.innerHTML = '<span class="empty">no agents running</span>';
  } else {
    al.innerHTML = d.worktrees.map(w =>
      `<div class="agent-item">
        <span class="agent-id">${w.id}</span>
        <span class="agent-commit">${escHtml(w.last_commit)}</span>
      </div>`
    ).join('');
  }

  // locks
  const ll = document.getElementById('locks-list');
  if (d.locks.length === 0) {
    ll.innerHTML = '<span class="empty">no active locks</span>';
  } else {
    ll.innerHTML = d.locks.map(l =>
      `<div class="lock-item">
        <span class="lock-task">${escHtml(l.task)}</span>
        <span class="lock-owner">${escHtml(l.owner)}</span>
      </div>`
    ).join('');
  }

  // tasks
  document.getElementById('tasks-content').textContent = d.tasks_content || '(empty)';

  // git log
  document.getElementById('git-log').innerHTML = formatGitLog(d.git_log);

  // log tabs
  const tabs = document.getElementById('log-tabs');
  if (d.recent_logs.length > 0) {
    tabs.innerHTML = d.recent_logs.map((l, i) =>
      `<button class="log-tab ${i === currentLogIndex ? 'active' : ''}"
              onclick="selectLog(${i})">${l.file.replace('agent_','').replace('.log','')}</button>`
    ).join('');
    showLog(d.recent_logs[currentLogIndex]);
  } else {
    tabs.innerHTML = '';
    document.getElementById('log-content').textContent = 'no logs yet';
  }

  // pending input
  const pi = document.getElementById('pending-input');
  if (d.human_input) {
    pi.textContent = `Pending: ${d.human_input}`;
  } else {
    pi.textContent = '';
  }
}

function selectLog(i) {
  currentLogIndex = i;
  if (statusData) {
    document.querySelectorAll('.log-tab').forEach((t, j) =>
      t.classList.toggle('active', j === i));
    showLog(statusData.recent_logs[i]);
  }
}

function showLog(log) {
  const el = document.getElementById('log-content');
  el.textContent = log ? log.tail : 'empty';
  el.scrollTop = el.scrollHeight;
}

async function sendInput() {
  const input = document.getElementById('human-input');
  const msg = input.value.trim();
  if (!msg) return;

  const btn = document.getElementById('send-btn');
  btn.disabled = true;
  btn.textContent = '...';

  try {
    const res = await fetch('/api/input', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: msg})
    });
    const data = await res.json();
    if (data.ok) {
      showToast('Command sent!');
      input.value = '';
      fetchStatus();
    }
  } catch(e) {
    showToast('Send failed: ' + e);
  } finally {
    btn.disabled = false;
    btn.textContent = '发送';
  }
}

async function stopSwarm() {
  if (!confirm('确定要停止所有agent吗？')) return;
  try {
    const res = await fetch('/api/stop', {method: 'POST'});
    const data = await res.json();
    showToast(data.message || 'Stopped');
    setTimeout(fetchStatus, 1000);
  } catch(e) {
    showToast('Stop failed: ' + e);
  }
}

// Auto refresh
fetchStatus();
setInterval(fetchStatus, 5000);
</script>
</body>
</html>"""


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # 静默日志

    def do_GET(self):
        if self.path == "/api/status":
            self.send_json(get_status())
        elif self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(DASHBOARD_HTML.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode() if content_length else "{}"

        if self.path == "/api/input":
            try:
                data = json.loads(body)
                result = send_human_input(data.get("message", ""))
                self.send_json(result)
            except Exception as e:
                self.send_json({"ok": False, "error": str(e)})

        elif self.path == "/api/stop":
            try:
                skill_dir = Path(__file__).parent.parent
                run_cmd(f"bash {skill_dir}/scripts/stop_swarm.sh {PROJECT_DIR}")
                self.send_json({"ok": True, "message": "蜂群已停止"})
            except Exception as e:
                self.send_json({"ok": False, "error": str(e)})
        else:
            self.send_response(404)
            self.end_headers()

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())


if __name__ == "__main__":
    print(f"🐝 蜂群观测台启动")
    print(f"   项目: {PROJECT_DIR}")
    print(f"   地址: http://localhost:{PORT}")
    print(f"   按 Ctrl+C 停止")
    print()

    server = http.server.HTTPServer(("0.0.0.0", PORT), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n观测台已关闭")
        server.server_close()
