# watcher.py
import subprocess
import sys
from watchfiles import watch

def run_script():
    subprocess.run([sys.executable, "if_statements.py"])

if __name__ == "__main__":
    for changes in watch('.', watch_filter=lambda change, path: path.endswith('.py')):
        run_script()
