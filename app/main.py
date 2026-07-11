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


def main():
    print("=" * 36)
    print("JARVIS Mission Command v0.2")
    print("=" * 36)
    print()

    print("Initializing Mission Academy...")
    print("Loading Cadet Database...")
    print("Loading Robotics Systems...")
    print("Loading Mission Database...")
    print("Loading JARVIS Core...")

    cadets = load_cadets()

    print()
    print("[OK] Mission Academy Online")
    print("[OK] Cadet Database Online")
    print("[OK] Robotics Systems Online")
    print("[OK] Mission Database Online")
    print("[OK] JARVIS Core Online")
    print()
    print("Welcome Commander Miller.")
    print()
    print("{} cadets registered:".format(len(cadets)))

    for cadet in cadets:
        name = cadet.get("name", "Unknown Cadet")
        call_sign = cadet.get("call_sign", "Unassigned")
        print("- {} ({})".format(name, call_sign))

    print()
    print("Awaiting orders...")


if __name__ == "__main__":
    main()
