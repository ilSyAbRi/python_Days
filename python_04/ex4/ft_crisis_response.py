def crisis_handler(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read().strip()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("\nRESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stabilized")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archive.txt")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    crisis_handler("classified_vault.txt")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
