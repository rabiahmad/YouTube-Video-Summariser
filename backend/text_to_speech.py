from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(input_text):
    language = 'en'

    # save tts as mp3 file
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save("reading.mp3")
    os.system("mpg321 reading.mp3")

    # this reads it out the mp3 file
    playsound('reading.mp3')

if __name__ == "__main__":
    text_to_speech(" Hello, This is a speech to text.")
