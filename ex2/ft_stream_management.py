from sys import stdin, stdout, stderr


def stream_managment() -> None:
    """
    Simulates a multi-channel communication test using standard system streams.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    arch_id = input("Input Stream active. Enter archivist ID: ")

    stdout.write("Input Stream active. Enter status report: ")
    stdout.flush()
    report_status = stdin.readline()

    stdout.write(f"[STANDARD] Archive status from {arch_id}: {report_status}")
    stderr.write("[ALERT] System diagnostic: Communication channels verified")
    stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful")


if __name__ == "__main__":
    stream_managment()
