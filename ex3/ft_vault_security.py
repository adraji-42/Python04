def main(filename: str) -> None:
    """Performs a secure read/write operation on the specified vault file."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    try:
        with open(filename, "r") as vault:
            print("SECURE EXTRACTION:")
            content = vault.read()
            print(content, end="\n\n")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")

    try:
        with open(filename, "w") as vault:
            print("SECURE PRESERVATION:")
            vault.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
            vault.write("Vault automatically sealed upon completion\n")
            print("Vault automatically sealed upon completion")
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main("vault.txt")
