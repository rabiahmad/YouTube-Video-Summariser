import pyttsx3


def text_to_speech(input_text):
    engine = pyttsx3.init()
    engine.say(str(input_text))
    engine.runAndWait()


if __name__ == "__main__":
    text_to_speech(" Hello, This is a speech to text.")
