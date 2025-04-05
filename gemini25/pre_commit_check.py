import subprocess
import sys


def run_command(command: str, description: str) -> None:
    """Run a shell command and print its status."""
    print(f"Running {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"{description} failed. Please fix the issues and try again.")
        sys.exit(result.returncode)
    print(f"{description} completed successfully.\n")


def main() -> None:
    # Run mypy for type checking
    run_command("mypy .", "mypy (type checking)")

    # Run black for code formatting
    run_command("black .", "black (code formatting)")

    # Run ruff for linting
    run_command("ruff .", "ruff (linting)")

    print("All checks passed! You can now commit your changes.")


if __name__ == "__main__":
    main()
