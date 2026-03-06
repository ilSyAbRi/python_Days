if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("oh shit PermissionError here we go again")
