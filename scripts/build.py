import os
import platform
import subprocess
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "python-dotenv"], check=True)
    from dotenv import load_dotenv

try:
    import PyInstaller
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)

PROJECT_NAME = os.getenv("PROJECT_NAME", "PythonTemplate")
ENTRY_FILE = os.getenv("ENTRY_FILE", "src/main.py")

hidden_imports = []
req_file = Path("requirements.txt")
if req_file.exists():
    with open(req_file) as f:
        for line in f:
            pkg = line.strip().split("==")[0]
            if pkg:
                hidden_imports.append("--hidden-import")
                hidden_imports.append(pkg)

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def build_for_current_os():
    system = platform.system().lower()
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--console",
        "--name", PROJECT_NAME,
        ENTRY_FILE,
        "--paths", "src"
    ] + hidden_imports
    if env_path.exists():
        cmd += ["--add-data", f"{env_path};."] if system == "windows" else ["--add-data", f"{env_path}:."]
    run_command(cmd)
    print(f"✅ Build completed for {system}")
    print(f"👉 Executable location: dist/{PROJECT_NAME}{'.exe' if system == 'windows' else ''}")
    print(f"👉 Test command: {'dist\\\\' + PROJECT_NAME + '.exe' if system == 'windows' else './dist/' + PROJECT_NAME}")

if __name__ == "__main__":
    print(f"Detected OS: {platform.system()}")
    build_for_current_os()