import os
import random
import threading

import pyttsx3
import speech_recognition as sr

import speak
import settings

r = sr.Recognizer()
tekst = [
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "ccccccccccccccccccccccccccccccccccccccccccccccccccc",
]


def takeCommand():
    with sr.Microphone() as source:

        print("Słuchanie...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rozpoznawanie...")
        query = r.recognize_google(audio, language="pl-pl")
        print(f"Użytkownik powiedział: {query}\n")

    except Exception as e:
        print(e)
        print("Nie można odczytać głosu.")
        return "None"

    return query


def xd():
    print("xd")
    t = random.choice(tekst)
    x = threading.Thread(target=speak.say, args=(t,))
    x.start()


if __name__ == "__main__":
    settings.create_init()
    clear = lambda: os.system("cls")
    clear()
    speak.welcome()

    while True:

        query = takeCommand().lower()

        if "siema" in query:
            x = threading.Thread(target=xd)
            x.start()
