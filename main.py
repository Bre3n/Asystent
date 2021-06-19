import json
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
keywords = []


def takeCommand():
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio, language=bufor)
        print(f"User say: {query}\n")

    except Exception as e:
        print("Unable to recognize.", e)
        return "None"

    return query


if __name__ == "__main__":
    settings.check_file()
    clear = lambda: os.system("cls")
    clear()
    speak.welcome()
    with open("settings.json") as json_file:
        data = json.load(json_file)
        for p in data["settings"]:
            bufor = p["language"]
    with open(f"languages/{bufor}.json") as json_file:
        data = json.load(json_file)
        a = len(data["keywords"][0])
        for p in data["keywords"]:
            for i in range(a):
                keywords.append(p[f"{i+1}"])
    print(keywords)

    while True:
        query = takeCommand().lower()
        if "siema" in query:
            t = random.choice(tekst)
            x = threading.Thread(target=speak.say, args=(t,))
            x.start()
