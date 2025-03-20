import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and exit on failure."""
    process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(process.stdout)
    if process.stderr:
        print(process.stderr, file=sys.stderr)

def main():
    """Execute deployment tasks for Render."""
    # Install dependencies
    print("Installing dependencies...")
    run_command("pip install -r requirements.txt")

    # Collect static files
    print("Collecting static files...")
    run_command("python manage.py collectstatic --noinput")

    # Run database migrations
    print("Running migrations...")
    run_command("python manage.py migrate")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}", file=sys.stderr)
        sys.exit(1)