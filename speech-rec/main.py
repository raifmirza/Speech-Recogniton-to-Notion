import speech_recognition as sr
import gtts 
from playsound import playsound
import os
from datetime import datetime
from notion import NotionClient

token = "secret_fHdqhntGJ5KtaZeBsW0fzrfupGgfUkrH3bYdawRmvkT"
database = "d88be45257434a65877e75b29fc42bc4"
r = sr.Recognizer()
activation_command = "hello"

client = NotionClient(token,database)
def get_audio():
    with sr.Microphone() as source:
        print("Say Something..")
        audio = r.listen(source)
        return audio

 
def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError:
        print("Could not request results from API")
    
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("Could not play the sound.")

if __name__ == "__main__":
    a = get_audio()
    command = audio_to_text(a)
    
    if activation_command in command.lower():
        print("Activated... You can speak now.")
        #play_sound("What do you want?")

        note = get_audio()
        note = audio_to_text(note)

        if note:
            play_sound(note)

            now = datetime.now().astimezone().isoformat()
            res = client.create_page(note, now, status = "Active")
            if res.status_code == 200:
                play_sound("Stored new item.")



