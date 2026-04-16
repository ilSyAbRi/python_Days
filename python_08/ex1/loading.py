import sys


def do_check_and_import():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies...\n")

    try:
        global np, pd, plt, requests, matplotlib

        import numpy as np
        import pandas as pd
        import matplotlib
        import matplotlib.pyplot as plt
        import requests

        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")

    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e.name}")
        print("Install it using pip or poetry")
        sys.exit(1)


def do_generate_matrix():
    print("\nAnalyzing Matrix data...")

    data = np.random.randn(1000)
    print("Processing 1000 data points...")

    df = pd.DataFrame({"value": data})

    print("\nStatistical summary:")
    print(df.describe())

    plt.hist(data, bins=30)
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    do_check_and_import()
    do_generate_matrix()


if __name__ == "__main__":
    main()
