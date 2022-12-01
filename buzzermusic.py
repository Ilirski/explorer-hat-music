from itertools import groupby
from operator import itemgetter
from tones import tones_dict
from time import sleep, time
import explorerhat as hat
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("""Error importing RPi.GPIO!
            This is probably because you need superuser privileges.
            You can achieve this by using 'sudo' to run your script""")


def parse_song(file: str) -> list[tuple[int, str]]:
    # does not account for non integer beats and notes sadly
    # parses music notes copied from onlinesequencer.net
    timestamps = []
    notes = []
    with open(file, 'r') as f:
        midiSequence = f.readline()
        # remove first 17 characters and last 3 characters,
        cleanedSequence = midiSequence[17:-3]
        # then remove everything up to the first :
        cleanedSequence = cleanedSequence[cleanedSequence.find(':')+1:]
        splitSequence = cleanedSequence.split(";")
        for sequence in splitSequence:
            midiSplit = sequence.split(" ")
            beats = round(float(midiSplit[2]))  # access beats
            for beat in range(beats):
                timestamps.append(beat + round(float(midiSplit[0])))
                notes.append(midiSplit[1])

    # keep sorted
    ungroupednotes = sorted(list(zip(timestamps, notes)))

    # grouping tuples by first element
    # taken from
    # https://stackoverflow.com/questions/45476509/group-list-of-tuples-efficiently
    groupednotes = [(k, [x for _, x in g])
                    for k, g in groupby(ungroupednotes, itemgetter(0))]

    # add silence
    for i in range(len(groupednotes) - 1):
        if groupednotes[i][0] != groupednotes[i+1][0] - 1:
            for num in range(groupednotes[i][0], groupednotes[i+1][0]):
                groupednotes.append((num, ["P"]))

    sortedgroupednotes = sorted(groupednotes)
    return sortedgroupednotes


def play_tones(tones: list[str, ...], beatduration: float):
    num_freq = len(tones)
    t_end = time() + beatduration
    while time() < t_end:  # play for length of beat duration
        for j in range(num_freq):
            buzzer.ChangeFrequency(tones_dict[tones[j]])
            buzzer.start(50)
            # how many times to repeat each note
            sleep(beatduration / (3 * num_freq))
        buzzer.stop()


def play_silence(beatduration: float):
    # Stops buzzer from playing
    sleep(beatduration / 2)
    buzzer.stop()


def play_song(song: list[tuple[int, str]],
              beatduration: float = 0.12,
              is_led: bool = True):
    # song: output of parse_song function
    # beatduration: change how long each beat plays
    # is_led: enable or disable led

    # Sets up GPIO pin 18 as a PWM output
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    global buzzer
    buzzer = GPIO.PWM(18, 500)

    for i in range(len(song)):
        notes_to_play = song[i][1]
        print(str(song[i][0]) + ": " + str(notes_to_play))
        tone = notes_to_play[0]
        if tone == "P":
            play_silence(beatduration)
            hat.output.off()
        else:
            play_tones(notes_to_play, beatduration)
            if is_led:
                if len(notes_to_play) == 1:
                    hat.output.off()
                    hat.output.three.on()
                elif len(notes_to_play) == 2:
                    hat.output.off()
                    hat.output.three.on()
                    hat.output.two.on()
                else:
                    hat.output.off()
                    hat.output.three.on()
                    hat.output.two.on()
                    hat.output.one.on()
    print("End :)")
