if __name__ == "__main__":

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with (
        open("classified_data.txt", "r") as vault1,
        open("standard_archive.txt", "r") as vault2
        ):
            content1 = vault1.read()
            content2 = vault2.read()
            print(content1)
            print(content2)
            print("Vault automatically sealed upon completion")
    except FileNotFoundError:
        print("{[}CLASSIFIED{]} Vault missing! Extraction failed\n")
    except PermissionError:
        print("oh shit PermissionError here we go again")
