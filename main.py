import asyncio
import datetime
import json
import multiprocessing
import os
import random
import time
from os import listdir
from os.path import isfile, join

import speech_recognition as sr

import module_main
import settings
import speak

r = sr.Recognizer()
keywords = []
text = []


def takeCommand(language):
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognition...")
        query = r.recognize_google(audio, language=language)
        print(f"User say: {query}\n")
    except Exception as e:
        print("Unable to recognize.", e)
        return "None"
    return query


if __name__ == "__main__":
    settings.check_file()
    os.system("cls" if os.name == "nt" else "clear")
    with open("settings.json") as json_file:
        data = json.load(json_file)
        for p in data["settings"]:
            username = p["username"]
            language = p["language"]
    onlyfiles = [f for f in listdir("languages") if isfile(join("languages", f))]
    bufor = any(p in f"{language}.json" for p in onlyfiles)
    if bufor == False:
        print(
            "Unable to find language file. Try again or check if language is properly set!"
        )
        time.sleep(10)
        exit()
    with open(f"languages/{language}.json") as json_file:
        data = json.load(json_file)
        a = len(data["keywords"][0])
        for p in data["keywords"]:
            for i in range(a):
                keywords.append(p[f"{i+1}"].lower())
        a = len(data["keywords"][0])
        for p in data["text"]:
            for i in range(a):
                text.append(p[f"{i+1}"].lower())
        print(keywords)
        print(text)
        print("\n")
        speak.welcome(text[0])

    while True:
        query = takeCommand(language).lower()
        if keywords[0] in query:  # * 1 good morning
            x = multiprocessing.Process(
                target=speak.say, args=(f"{text[0]} {username}",)
            ).start()

        elif keywords[1] in query:  # * 2 hello
            x = multiprocessing.Process(target=speak.say, args=({text[1]},)).start()

        elif keywords[2] in query:  # * 3 change username
            words = text[2]
            bufor = text[2].split("&")
            asyncio.run(module_main.change_username(bufor, language))

        elif keywords[3] in query:  # * 4 time
            strTime = datetime.datetime.now().strftime("%H:%M")
            x = multiprocessing.Process(
                target=speak.say, args=(f"{text[3]}{strTime}",)
            ).start()

        elif keywords[4] in query:  # * 5 date
            strTime = datetime.datetime.now().strftime("%d")
            x = multiprocessing.Process(
                target=speak.say, args=(f"{text[4]}{strTime}",)
            ).start()

        elif keywords[5] in query:  # * 6 ok google
            bufor = text[5].split("&")
            x = multiprocessing.Process(
                target=speak.say, args=({random.choice(bufor)},)
            ).start()

        elif keywords[6] in query:  # * 7 alexa
            bufor = text[6].split("&")
            x = multiprocessing.Process(
                target=speak.say, args=({random.choice(bufor)},)
            ).start()
