def create_new_archive(filename: str = "new_discovery.txt") -> None:
    """Establishes a new storage unit and inscribes preservation data."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")

    vault = open(filename, 'w')

    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    try:
        entries = [
            "New quantum algorithm discovered",
            "Efficiency increased by 347%",
            "Archived by Data Archivist trainee"
        ]

        i = 1
        for content in entries:
            entry_line = f"[ENTRY {i:03}] {content}\n"

            vault.write(entry_line)
            print(entry_line.strip())
            i += 1
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")
    finally:
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")

    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        create_new_archive()
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")
