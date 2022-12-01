from buzzermusic import parse_song, play_song
from time import time
import argparse
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("""Error importing RPi.GPIO!
            This is probably because you need superuser privileges.
            You can achieve this by using 'sudo' to run your script""")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Play any song from onlinesequencer.net "
                        "with a buzzer on the Raspberry Pi!")

    parser.add_argument('filename',
                        type=str,
                        help=".txt file containing notes "
                             "copied from onlinesequencer.net")
    args = parser.parse_args()
    file = args.filename

    try:
        start_time = time()
        song = parse_song(file)
        play_song(song, 0.125)
    except KeyboardInterrupt:
        print("Keyboard Interrupt, exiting")
    except (ValueError, IndexError):
        print("File not in the correct format, ensure that your file is a "
              ".txt file and it only contains notes copypasted "
              "from onlinesequencer.net (and check for trailing spaces)")
    except FileNotFoundError:
        print("File not found, ensure that file is in "
              "the same folder as music.py")
    finally:
        print(f"Elapsed time: {time() - start_time:.2f} seconds")
        GPIO.cleanup(18)
