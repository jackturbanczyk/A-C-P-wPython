# Git Automation with Aliases

This project provides a Python script (`add-commit-push.py`) to automate common Git commands (add, commit, and push).

## How to Use

1. **Run the script**:

    ```bash
    python add-commit-push.py /path/to/your/project -m "Your commit message"
    ```

    If no commit message is provided, it defaults to `"Auto commit"`:

    ```bash
    python add-commit-push.py /path/to/your/project
    ```

2. **Use the force flag** (`-f`) to skip confirmation:

    ```bash
    python add-commit-push.py /path/to/your/project -m "Your commit message" -f
    ```

## Aliases

To simplify usage, you can set up the following aliases in your shell configuration file (e.g., `.bashrc`, `.zshrc`):

```bash
# Alias for navigating to the sprint-5 folder
alias g5='cd /path/to/your/sprint-5/folder'

# Alias for running the add-commit-push.py script from any directory
alias acp='python /path/to/add-commit-push.py'
