if __name__ == "__main__":

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with (
            open("classified_data.txt", "r") as vault1,
            open("security_protocols.txt", "r") as vault2
        ):
            content1 = vault1.read()
            content2 = vault2.read()
            print("\nSECURE EXTRACTION:")
            print(content1)
            print("\nSECURE PRESERVATION:")
            print(content2)
            print("Vault automatically sealed upon completion")
            print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print("\n{[}CLASSIFIED{]} Vault missing! Extraction failed\n")
    except PermissionError:
        print("\noh shit PermissionError here we go again")
