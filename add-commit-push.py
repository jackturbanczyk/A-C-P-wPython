#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse

def run_command(command: list):
    print(f"Executing: {' '.join(command)}\n")
    result = subprocess.run(command, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

def change_directory(path: str):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}\n")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        sys.exit(1)

def git_status():
    print("git status:\n")
    run_command(["git", "status"])

def git_add():
    print("Queued command: git add .\n")

def git_commit(message: str):
    print(f"Queued command: git commit -m '{message}'\n")

def git_push():
    """Push the committed changes."""
    print("Queued command: git push\n")

def confirm_execution():
    """Prompt the user for confirmation to execute the queued commands."""
    confirm = input("Do you want to execute these commands? (y/n): ")
    if confirm.lower() != 'y':
        print("Aborted by user.")
        sys.exit(0)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Automate git add, commit, and push.")
    parser.add_argument("-m", "--message", type=str, default="Auto commit",
                        help="Commit message. Defaults to 'Auto commit'.")
    parser.add_argument("project_path", type=str, help="Path to the project directory.")
    parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation prompt.")

    args = parser.parse_args()

    # Change to the project directory
    change_directory(args.project_path)

    # Display git status
    git_status()

    # Queue commands
    git_add()
    git_commit(args.message)
    git_push()

    if not args.force:
        confirm_execution()

    print("Staging changes...\n")
    run_command(["git", "add", "."])

    print(f"Committing changes with message: '{args.message}'...\n")
    run_command(["git", "commit", "-m", args.message])

    print("Pushing changes to remote...\n")
    run_command(["git", "push"])

if __name__ == "__main__":
    main()
