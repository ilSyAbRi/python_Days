import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

archivist_id = input("\nInput Stream active. Enter archivist ID: ")

status_report = input("Input Stream active. Enter status report: ")

print(f"\n{{[}}STANDARD{{]}} Archive status"
      f"from {archivist_id}: {status_report}")

sys.stderr.write("{[}ALERT{]} System diagnostic: "
                 "Communication channels verified\n")

print("{[}STANDARD{]} Data transmission complete")

print("\nThree-channel communication test successful.")
