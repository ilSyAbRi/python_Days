try:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    print("RECOVERED DATA:")
    print(file.read())
    file.close()
    print("Data recovery complete. Storage unit disconnected.")
except:
    print("ERROR: Storage vault not found. Run data generator first.")