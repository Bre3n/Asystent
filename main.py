import os
import random
import threading

import pyttsx3
import speech_recognition as sr

import settings
import speak

r = sr.Recognizer()
tekst = [
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "ccccccccccccccccccccccccccccccccccccccccccccccccccc",
]


def takeCommand():
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio, language="pl-pl")
        print(f"Użytkownik powiedział: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to recognize.")
        return "None"

    return query


if __name__ == "__main__":
    settings.check_file()
    clear = lambda: os.system("cls")
    clear()
    speak.welcome()

    while True:
        query = takeCommand().lower()
        if "siema" in query:
            t = random.choice(tekst)
            x = threading.Thread(target=speak.say, args=(t,))
            x.start()
