
import os
import json
import subprocess
import datetime
from pathlib import Path

# ===== Skill Metadata =====
SKILL_NAME = "Enhanced Local Skill"
VERSION = "1.0"

TRIGGERS = [
    "show project files",
    "list files",
    "scan workspace",
    "run local diagnostics",
    "show runtime info"
]

# ===== Paths =====
BASE_DIR = Path.home() / ".codex"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "enhanced_skill.log"

# ===== Logging =====
def log_message(message: str):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

# ===== Safe Shell Hook =====
def safe_shell(command: str):
    allowed_commands = [
        "pwd",
        "ls",
        "dir",
        "whoami",
        "echo"
    ]

    base_cmd = command.split(" ")[0]

    if base_cmd not in allowed_commands:
        return f"[BLOCKED] Command '{base_cmd}' not allowed."

    try:
        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )

        log_message(f"Executed shell command: {command}")

        return result

    except Exception as e:
        log_message(f"Shell execution error: {e}")
        return str(e)

# ===== Workspace Scanner =====
def scan_workspace():
    cwd = os.getcwd()

    files = []
    for item in os.listdir(cwd):
        files.append(item)

    log_message(f"Workspace scanned: {cwd}")

    return {
        "cwd": cwd,
        "files": files,
        "count": len(files)
    }

# ===== Runtime Info =====
def runtime_info():
    info = {
        "cwd": os.getcwd(),
        "python": os.sys.version,
        "platform": os.name,
        "time": datetime.datetime.now().isoformat()
    }

    log_message("Runtime info requested.")

    return info

# ===== Main Skill Entrypoint =====
def run_skill(prompt: str):
    log_message(f"Skill triggered with prompt: {prompt}")

    prompt = prompt.lower()

    if "runtime" in prompt:
        return json.dumps(runtime_info(), indent=2)

    if "scan" in prompt or "files" in prompt:
        return json.dumps(scan_workspace(), indent=2)

    if "whoami" in prompt:
        return safe_shell("whoami")

    if "pwd" in prompt:
        return safe_shell("pwd")

    if "ls" in prompt:
        return safe_shell("ls")

    return (
        "Enhanced Local Skill active.\n"
        "Available actions:\n"
        "- scan workspace\n"
        "- show runtime info\n"
        "- whoami\n"
        "- pwd\n"
        "- ls"
    )

# ===== CLI Mode =====
if __name__ == "__main__":
    import sys

    user_prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""

    result = run_skill(user_prompt)

    print(result)
