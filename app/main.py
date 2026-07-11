import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CADETS_DIR = os.path.join(BASE_DIR, "cadets")


def load_cadets():
    cadets = []

    for filename in sorted(os.listdir(CADETS_DIR)):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(CADETS_DIR, filename)

        with open(path, "r") as cadet_file:
            cadets.append(json.load(cadet_file))

    return cadets


def show_status():
    print()
    print("SYSTEM STATUS")
    print("[OK] Mission Academy Online")
    print("[OK] Cadet Database Online")
    print("[OK] Robotics Systems Online")
    print("[OK] Mission Database Online")
    print("[OK] JARVIS Core Online")
    print()


def show_cadets(cadets):
    print()
    print("{} cadets registered:".format(len(cadets)))

    for cadet in cadets:
        name = cadet.get("name", "Unknown Cadet")
        call_sign = cadet.get("call_sign", "Unassigned")
        print("- {} ({})".format(name, call_sign))

    print()


def show_help():
    print()
    print("AVAILABLE COMMANDS")
    print("help    - Show available commands")
    print("status  - Show Mission Academy system status")
    print("cadets  - Show registered cadets")
    print("clear   - Clear the screen")
    print("exit    - Shut down JARVIS command interface")
    print()


def command_loop(cadets):
    while True:
        command = input("JARVIS> ").strip().lower()

        if command == "help":
            show_help()
        elif command == "status":
            show_status()
        elif command == "cadets":
            show_cadets(cadets)
        elif command == "clear":
            os.system("clear")
        elif command == "exit":
            print()
            print("JARVIS: Command interface shutting down.")
            break
        elif command == "":
            continue
        else:
            print("JARVIS: Command not recognized. Type 'help'.")


def main():
    print("=" * 40)
    print("JARVIS Mission Command v0.3")
    print("=" * 40)
    print()

    print("Initializing Mission Academy...")
    print("Loading Cadet Database...")
    print("Loading Robotics Systems...")
    print("Loading Mission Database...")
    print("Loading JARVIS Core...")
    print()

    cadets = load_cadets()

    show_status()

    print("Welcome Commander Miller.")
    show_cadets(cadets)

    print("Type 'help' to view available commands.")
    print()

    command_loop(cadets)


if __name__ == "__main__":
    main()
