import os
import time
import wave
import threading
from piper import PiperVoice


MODEL = "/home/rooster/en_US-lessac-medium.onnx"
SAMPLE_RATE = 22050

MISSION_TEXT = (
    "Mission 001: First Fabrication. "
    "Cadets Teddy and Karla. "
    "Your objective is to manufacture your first Mission Academy artifact using the 3D printer. "
    "Mission objectives: "
    "Choose one object that you think is awesome. "
    "Prepare the object for printing. "
    "Send it to the fabrication lab. "
    "Inspect the completed print. "
    "Recommended builds: "
    "Articulated dragon. "
    "Flexi dinosaur. "
    "Minecraft figure. "
    "GOOSE or PHOENIX nameplate. "
    "Reward: Qualification 001: Fabrication Recruit. "
    "Report to Commander Dad after your first successful print."
)

voice = PiperVoice.load(MODEL, use_cuda=False)


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


def get_word_timings(text):
    chunks = list(
        voice.synthesize(
            text,
            include_alignments=True
        )
    )

    alignments = []

    for chunk in chunks:
        if chunk.phoneme_alignments:
            alignments.extend(chunk.phoneme_alignments)

    words = text.split()

    groups = []
    current_word = []
    current_time = 0.0

    for item in alignments:
        duration = item.num_samples / SAMPLE_RATE
        phoneme = item.phoneme

        if phoneme == " ":
            if current_word:
                groups.append(
                    (
                        "".join(current_word),
                        current_time
                    )
                )
                current_word = []
        else:
            current_word.append(phoneme)

        current_time += duration

    if current_word:
        groups.append(
            (
                "".join(current_word),
                current_time
            )
        )

    timings = []
    word_index = 0

    for i, group in enumerate(groups):
        if word_index >= len(words):
            break

        group_start = group[1]

        if i + 1 < len(groups):
            group_end = groups[i + 1][1]
        else:
            group_end = current_time

        remaining_words = len(words) - word_index
        remaining_groups = len(groups) - i

        if remaining_words == remaining_groups:
            timings.append(
                (words[word_index], group_start)
            )
            word_index += 1
            continue

        words_to_split = 2
        selected = words[word_index:word_index + words_to_split]

        total_chars = sum(len(w) for w in selected)

        if total_chars == 0:
            continue

        span = group_end - group_start
        cursor = group_start

        for j, word in enumerate(selected):
            timings.append((word, cursor))

            if j < len(selected) - 1:
                portion = span * (len(word) / total_chars)
                cursor += portion

            word_index += 1

    if len(timings) < len(words):
        last_time = timings[-1][1] if timings else 0.0

        while len(timings) < len(words):
            timings.append(
                (words[len(timings)], last_time)
            )

    return words, timings


def create_audio(text, filename):
    with open(filename, "wb") as f:
        wav = wave.open(f, "wb")
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)

        for chunk in voice.synthesize(text):
            wav.writeframes(chunk.audio_int16_bytes)

        wav.close()


def highlight_and_speak(text):
    audio_file = "/tmp/jarvis_mission.wav"

    words, timings = get_word_timings(text)

    # Generate the complete audio before beginning the display.
    create_audio(text, audio_file)

    def play_audio():
        os.system(
            f"aplay -q {audio_file}"
        )

    speaker_thread = threading.Thread(target=play_audio)
    speaker_thread.start()

    time.sleep(0.05)

    clear_screen()

    print("=" * 48)
    print("             MISSION BRIEFING")
    print("=" * 48)
    print()
    print("JARVIS AUDIO BRIEFING")
    print()

    start_time = time.monotonic()

    for i, word in enumerate(words):
        if i >= len(timings):
            break

        target = timings[i][1]

        while True:
            elapsed = time.monotonic() - start_time
            remaining = target - elapsed

            if remaining <= 0:
                break

            time.sleep(min(0.005, remaining))

        print("\r\033[K", end="")

        for j, w in enumerate(words):
            if j == i:
                print(f"\033[93m{w}\033[0m", end="")
            else:
                print(w, end="")

            if j < len(words) - 1:
                print(" ", end="")

        print("   ", end="", flush=True)

    speaker_thread.join()

    print()
    print()
    print("JARVIS: Mission briefing complete.")
    print()


def mission_briefing():
    highlight_and_speak(MISSION_TEXT)

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
    print("JARVIS: Report to Commander Dad after your")
    print("first successful print.")
    print()

    input("Press ENTER to return to Mission Control...")


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
