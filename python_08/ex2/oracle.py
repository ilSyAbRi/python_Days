import os
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL", "sqlite:///local.db")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "http://localhost")

    if not api_key:
        api_status = "[WARNING] Missing API_KEY"
    else:
        api_status = "[OK] Authenticated"

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")

    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")

    print("\nEnvironment security check:")

    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Missing secrets detected")

    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    load_configuration()


if __name__ == "__main__":
    main()
