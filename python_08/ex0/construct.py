import sys
import os
import site


def is_venv():
    return sys.prefix != sys.base_prefix

def main():
    if is_venv():
        print("MATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python:", sys.executable)

        env_name = os.path.basename(sys.prefix)
        print("Virtual Environment:", env_name)
        print("Environment Path:", sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        for p in sys.path:
            if "site-packages" in p:
                print("\nPackage installation path:")
                print(p)
                break
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
