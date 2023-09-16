from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(input_text):
    language = 'en'

<<<<<<< Updated upstream
    # save tts as mp3 file
=======
    # Create the "data" folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Save the TTS as an MP3 file in the "data" folder
    mp3_file_path = os.path.join(data_folder, "reading.mp3")
>>>>>>> Stashed changes
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save("reading.mp3")
    os.system("mpg321 reading.mp3")

    # this reads it out the mp3 file
    playsound('reading.mp3')

if __name__ == "__main__":
    text_to_speech(" Hello, This is a speech to text.")
