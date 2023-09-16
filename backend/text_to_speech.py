from gtts import gTTS
from playsound import playsound
import os
import streamlit as st

def text_to_speech(input_text):
    language = 'en'
    
    # Define the path to the "data" folder one level above the current directory
    data_folder = os.path.join(os.path.pardir, "data")

    # Save the TTS as an MP3 file in the "data" folder
    mp3_file_path = os.path.join(data_folder, "reading.mp3")
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save("../data/reading.mp3")

    # Play the MP3 file
    absolute_mp3_path = os.path.abspath(mp3_file_path)
    
    # playsound(absolute_mp3_path)
    st.audio(absolute_mp3_path)

if __name__ == "__main__":
    text_to_speech("Hello, This is a speech to text.")
