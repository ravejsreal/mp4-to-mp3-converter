"""
MP4 to MP3 Converter
made by: ravejsreal
GitHub: https://github.com/ravejsreal/mp4-to-mp3-converter
"""

import os
import sys
from pathlib import Path

missing_packages = []

try:
    from pydub import AudioSegment
except Exception as e:
    missing_packages.append("pydub")

try:
    from colorama import Fore, Style, init
except Exception as e:
    missing_packages.append("colorama")

if missing_packages:
    print("=" * 60)
    print("ERROR: Missing required packages".center(60))
    print("=" * 60)
    print()
    print(f"Missing: {', '.join(missing_packages)}")
    print()
    print("Install with:")
    print("  pip install -r requirements.txt")
    print()

    install = input("Install missing packages now? (y/n): ").strip().lower()
    if install == 'y':
        print()
        print("Installing packages...")
        import subprocess
        result = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pydub", "colorama"],
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("Installation complete! Restarting script...")
            print()
            input("Press Enter to restart...")
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            print("Installation failed. Try running manually:")
            print("  pip install pydub colorama")
            print()
            input("Press Enter to exit...")
    else:
        input("Press Enter to exit...")
    sys.exit(1)

init(autoreset=True)
PURPLE = Fore.MAGENTA + Style.BRIGHT

class MP4toMP3Converter:
    def __init__(self):
        script_dir = Path(__file__).parent
        self.output_dir = script_dir / "output"
        self.output_dir.mkdir(exist_ok=True)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print(PURPLE + "=" * 60)
        print(PURPLE + "MP4 TO MP3 CONVERTER".center(60))
        print(PURPLE + "made by ravejsreal".center(60))
        print(PURPLE + "github.com/ravejsreal/mp4-to-mp3-converter".center(60))
        print(PURPLE + "=" * 60)
        print()

    def convert_to_mp3(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video not found: {video_path}")

        print(PURPLE + "Loading video file...")
        audio = AudioSegment.from_file(video_path, format="mp4")

        duration = len(audio) / 1000
        print(PURPLE + f"Audio duration: {int(duration // 60)}m {int(duration % 60)}s")

        input_file = Path(video_path)
        output_path = self.output_dir / f"{input_file.stem}.mp3"

        print(PURPLE + "Extracting audio to MP3...")
        print(PURPLE + "This may take a moment depending on video length...")

        audio.export(str(output_path), format="mp3", bitrate="192k")

        return output_path

    def run(self):
        while True:
            self.print_header()

            print(PURPLE + "Convert MP4 video to MP3 audio")
            print()

            video_path = input(PURPLE + "Enter MP4 file path (or 'q' to quit): ").strip().strip('"')

            if video_path.lower() == 'q':
                print(PURPLE + "\nGoodbye!")
                break

            if not os.path.exists(video_path):
                print(PURPLE + f"\nError: File not found at {video_path}")
                print(PURPLE + "Press Enter to continue...")
                input()
                continue

            if not video_path.lower().endswith('.mp4'):
                print(PURPLE + "\nError: File must be an MP4 video")
                print(PURPLE + "Press Enter to continue...")
                input()
                continue

            try:
                print()
                print(PURPLE + "Converting MP4 to MP3...")
                print(PURPLE + "-" * 60)
                output_path = self.convert_to_mp3(video_path)
                print(PURPLE + "-" * 60)
                print(PURPLE + f"\n✓ SUCCESS!")
                print(PURPLE + f"  Output: {output_path}")

                input_size = os.path.getsize(video_path) / (1024 * 1024)
                output_size = os.path.getsize(output_path) / (1024 * 1024)
                print(PURPLE + f"  Input size: {input_size:.2f} MB")
                print(PURPLE + f"  Output size: {output_size:.2f} MB")

                print()
                open_folder = input(PURPLE + "Open output folder? (y/n): ").strip().lower()
                if open_folder == 'y':
                    os.startfile(self.output_dir)

                print()
                print(PURPLE + "Press Enter to continue...")
                input()

            except Exception as e:
                print(PURPLE + f"\n✗ Error: {e}")
                print(PURPLE + "Press Enter to continue...")
                input()


if __name__ == "__main__":
    converter = MP4toMP3Converter()
    converter.run()
