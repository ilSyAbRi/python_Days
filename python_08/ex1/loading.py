def do_check_and_import():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies...\n")

    try:
        global np, pd, plt, requests, matplotlib
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import matplotlib
        import requests
    except Exception as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("Install it using pip or poetry")
        exit()

def get_version():
    try:
        print(f"[OK] numpy ({np.__version__}) - ready")
        print(f"[OK] pandas ({pd.__version__}) - ready")
        print(f"[OK] matplotlib ({matplotlib.__version__}) - ready")
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except Exception as e:
        print(e)

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
    print("\nVisualization saved to: matrix_analysis.png")

def main():
    do_check_and_import()
    get_version()
    do_generate_matrix()

main()
