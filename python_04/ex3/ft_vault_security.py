if __name__ == "__main__":

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            content = vault.read()
            print(content, end="")
    except FileNotFoundError:
        print("{[}CLASSIFIED{]} Vault missing! Extraction failed\n")
    except PermissionError:
        print("oh shit pPermissionError here we go again")

    print("\nSECURE PRESERVATION:")
    try:
        with open("new_security_protocols.txt", "w") as vault:
            vault.write("{[}CLASSIFIED{]} New security protocols archived\n")
            print("{[}CLASSIFIED{]} New security protocols archived")

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except PermissionError:
        print("oh shit PermissionError here we go again")
