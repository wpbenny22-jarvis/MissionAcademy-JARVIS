import os
import time


def clear_screen():
    os.system("clear")


def pause(seconds=1):
    time.sleep(seconds)


def boot_sequence():
    clear_screen()

    print("=" * 48)
    print("        MISSION ACADEMY COMMAND")
    print("              JARVIS")
    print("=" * 48)
    print()

    print("Initializing Mission Academy...")
    pause()
    print("[OK] Cadet database online")
    pause()
    print("[OK] Fabrication lab online")
    pause()
    print("[OK] Mission control online")
    pause()
    print()
    print("JARVIS: Welcome, Cadets Teddy and Karla.")
    print()
    print("Type START to receive today's mission.")
    print()


def mission_briefing():
    clear_screen()

    print("=" * 48)
    print("             MISSION BRIEFING")
    print("=" * 48)
    print()
    print("MISSION 001: FIRST FABRICATION")
    print()
    print("Cadets Teddy and Karla,")
    print()
    print("Your objective is to manufacture your first")
    print("Mission Academy artifact using the 3D printer.")
    print()
    print("MISSION OBJECTIVES")
    print()
    print("1. Choose one object that you think is awesome.")
    print("2. Prepare the object for printing.")
    print("3. Send it to the fabrication lab.")
    print("4. Inspect the completed print.")
    print()
    print("RECOMMENDED BUILDS")
    print()
    print("- Articulated dragon")
    print("- Flexi dinosaur")
    print("- Minecraft figure")
    print("- GOOSE or PHOENIX nameplate")
    print()
    print("REWARD")
    print()
    print("Qualification 001: Fabrication Recruit")
    print()
    print("JARVIS: Report to Commander Dad to begin.")
    print()
    input("Press ENTER when the briefing is complete...")


def main():
    boot_sequence()

    while True:
        command = input("JARVIS> ").strip().lower()

        if command == "start":
            mission_briefing()
            boot_sequence()
        elif command == "briefing":
            mission_briefing()
            boot_sequence()
        elif command == "exit":
            print("JARVIS: Command interface shutting down.")
            break
        elif command == "":
            continue
        else:
            print("JARVIS: Type START to begin or EXIT to close.")


if __name__ == "__main__":
    main()
