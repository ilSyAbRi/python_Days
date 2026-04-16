import os
import sys
import site


def is_venv() -> bool:
    """Check if the script is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    """Extract the name of the virtual environment from the path."""
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    """Retrieve the primary site-packages path."""
    paths = site.getsitepackages()
    return paths[0] if paths else "Unknown"


def main() -> None:
    """Execute the environment detection logic."""
    in_matrix: bool = is_venv()
    if in_matrix:
        print("Inside the Construct")
        print("-" * 20)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage installation path:\n{get_package_path()}")
    else:
        print("Outside the Matrix")
        print("-" * 20)
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print(r"matrix_env\Scripts\activate     # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
