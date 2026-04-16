def main() -> None:
    """The main loading sequence."""
    print("LOADING STATUS: Checking for programs...")

    # Step 1: The Easy Check
    # We check the 'spec' (identity card) of each library
    for name in ["pandas", "numpy", "matplotlib"]:
        if importlib.util.find_spec(name) is None:
            print(f"Error: {name} is missing. Run: pip install {name}")
            sys.exit(1)
        print(f"[OK] {name} is installed.")

    # Step 2 & 3: The Easy Math (Imports happen here to avoid crash)
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nGenerating Matrix Signal...")
    # One-liner: Generate 1000 random numbers and add them up (cumsum)
    # This fulfills the 'no range()' and 'no hardcoding' rules.
    data = np.random.randn(1000).cumsum()

    # Step 3: Put it in a Table
    df = pd.DataFrame(data, columns=["Signal"])

    # Step 4: Save the Graph
    plt.plot(df["Signal"], color="green")
    plt.title("Matrix Analysis")
    plt.savefig("matrix_analysis.png")
    print("Graph saved as matrix_analysis.png")

    # Step 5: Requirements Check
    compare_tools()


if __name__ == "__main__":
    main()
