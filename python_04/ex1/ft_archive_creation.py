if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\nInitializing new storage unit: new_discovery.txt")

    try:
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        a = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
        b = "{[}ENTRY 002{]} Efficiency increased by 347%\n"
        c = "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
        file.write(a)
        file.write(b)
        file.write(c)
        file.close()
        print(a)
        print(b)
        print(c)
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("oh shit PermissionError error here we go again")
