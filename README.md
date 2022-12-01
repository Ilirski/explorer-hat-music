# explorer-hat-music-
Play music on a buzzer on your Explore Hat.

## Description
Play over 2.9 million songs available on onlinesequencer.net on a single buzzer on your Explorer Hat!

Multiple notes can be played at the same time by turning chords into very fast arpeggios, simulating a chord. 
Works best with simple songs (1—3 notes at a time). You can tell a song is too complex by adding green, yellow, and red LEDs, and then seeing whether the red LED lights up constantly throughout the song.

Made for a school project.

## Usage
1. Install Python 3.9 from https://www.python.org/downloads/release/python-390/
2. Write pip install requirements.txt into your command line (preferably in a virtual environment)
3. Go to https://onlinesequencer.net/sequences and search for a song
4. Once you found a song, click on the song and then press edit.
5. Copy all the notes (Ctrl A + Ctrl C or using the menu) and paste it in a .txt file as it is and save. Do not modify anything.
6. Place the .txt file in the same folder as music.py
7. Input python music.py <file name here> into your command line and music will play

## Credits
This project was heavily inspired by https://github.com/james1236/buzzer_music, meant for the Raspberry Pi Pico. The tones.py file was taken directly from his repository.
