# explorer-hat-music
Play music on a buzzer on your Explorer Hat.

## Description
Play over 2.9 million songs available on onlinesequencer.net on a single buzzer on your Raspberry Pi's Explorer Hat!

Multiple notes can be played at the same time by turning chords into very fast arpeggios, simulating the sound of chords playing. 
Works best with simple songs (either a note played at a time or chords consisting of two or three notes at a time). 
You can tell a song is too complex for the buzzer by adding green, yellow, and red LEDs. If the red LEDs light up constantly throughout the song, it is most probably too difficult to be played by the buzzer.

Made for a school project.

## Examples
- (Obligatory) Bad Apple: https://youtu.be/OS8dETCLiVI
- Yoru ni Kakeru: https://youtu.be/y2tyLgAHzRs
- Super Mario Brothers Theme Song: https://youtube.com/shorts/2k3WRzwtc_4?feature=share
- Katyusha: https://youtu.be/TSvroSVkahA

## Usage
1. Install Python 3.9 from https://www.python.org/downloads/release/python-390/
2. Write pip install requirements.txt into your command line (preferably in a virtual environment).
3. Go to https://onlinesequencer.net/sequences and search for a song.
4. Once you found a song, click on the song and then press the edit button.
5. Copy all the notes (Ctrl A + Ctrl C or using the menu) and paste it in a .txt file as it is and save. Do not modify anything.
6. Place the .txt file in the same folder as music.py
7. Input python music.py <file name here> into your command line and music will play.

## Credits
This project was heavily inspired by https://github.com/james1236/buzzer_music, meant for the Raspberry Pi Pico. The tones.py file was taken directly from his repository.
