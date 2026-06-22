def recover_ancient_data(filename: str = "ancient_fragment.txt") -> None:
    """Accesses the storage vault and recovers data fragments."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    vault = open(filename, 'r')

    print("Connection established...\n")

    try:
        content = vault.read()

        print("RECOVERED DATA:")

        i = 1
        for line in content.split('\n'):
            print(f"[FRAGMENT {i:03}] '{line.strip()}'")
            i += 1

        print("\nData recovery complete. ", end="")
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")
    finally:
        vault.close()
        print("Storage unit disconnected.")


if __name__ == "__main__":
    try:
        recover_ancient_data()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")
