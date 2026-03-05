if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ==="
    print("Initializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt","w")
    file.write("{[}ENTRY 001{]} New quantum algorithm discovered\n
                {[}ENTRY 002{]} Efficiency increased by 347%\n
                {[}ENTRY 003{]} Archived by Data Archivist trainee")
    file.close()
