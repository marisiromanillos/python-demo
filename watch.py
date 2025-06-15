# watcher.py
import subprocess
import sys
from watchfiles import watch

def run_script():
    subprocess.run([sys.executable, "functions.py"])

if __name__ == "__main__":
    for changes in watch('.', watch_filter=lambda change, path: path.endswith('.py')):
        print(f"Changes detected: {changes}")
        run_script()
