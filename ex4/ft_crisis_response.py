def handle_crisis(filename):
    """
    Simulates a system access attempt
    and manages potential failures gracefully.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    """Orchestrates a series of crisis response scenarios."""
    routine_files = ["standard_archive.txt"]
    crisis_files = ["lost_archive.txt", "classified_vault.txt"]

    for file in crisis_files:
        try:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            handle_crisis(file)
        except Exception as e:
            print(f"ERROR: An unexpected anomaly occurred: {e}")

    for file in routine_files:
        try:
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
            handle_crisis(file)
        except Exception as e:
            print(f"ERROR: An unexpected anomaly occurred: {e}")


if __name__ == "__main__":
    main()
