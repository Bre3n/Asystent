import asyncio
import datetime
import json
import multiprocessing
import os
import random
import subprocess
import time
import webbrowser
from os import listdir
from os.path import isfile, join
from shutil import which

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
    bufor = any(
        p in f"{language}.json"
        for p in [f for f in listdir("languages") if isfile(join("languages", f))]
    )
    if bufor == False:
        print(
            "Unable to find language file. Try again or check if language in settings.json is properly set!"
        )
        time.sleep(10)
        exit()
    with open(f"languages/{language}.json") as json_file:
        data = json.load(json_file)
        a = len(data["keywords"][0])
        for p in data["keywords"]:
            for i in range(a):
                keywords.append(p[f"{i}"].lower())
        a = len(data["keywords"][0])
        for p in data["text"]:
            for i in range(a):
                text.append(p[f"{i}"].lower())
        print(keywords)
        print(text)
        print("\n")
        speak.welcome(text[0])

    if username == "":
        bufor = text[2].split("&")
        asyncio.run(module_main.change_username(bufor, language))

    while True:
        query = takeCommand(language).lower()
        if keywords[0] in query:  # * 0 good morning
            multiprocessing.Process(
                target=speak.say, args=(f"{text[0]} {username}",)
            ).start()

        elif keywords[1] in query:  # * 1 hello
            multiprocessing.Process(target=speak.say, args=({text[1]},)).start()

        elif keywords[2] in query:  # * 2 change username
            bufor = text[2].split("&")
            asyncio.run(module_main.change_username(bufor, language))

        elif keywords[3] in query:  # * 3 time
            strTime = datetime.datetime.now().strftime("%H:%M")
            multiprocessing.Process(
                target=speak.say, args=(f"{text[3]}{strTime}",)
            ).start()

        elif keywords[4] in query:  # * 4 date
            strTime = datetime.datetime.now().strftime("%d")
            multiprocessing.Process(
                target=speak.say, args=(f"{text[4]}{strTime}",)
            ).start()

        elif keywords[5] in query:  # * 5 ok google
            bufor = text[5].split("&")
            multiprocessing.Process(
                target=speak.say, args=({random.choice(bufor)},)
            ).start()

        elif keywords[6] in query:  # * 6 alexa
            bufor = text[6].split("&")
            multiprocessing.Process(
                target=speak.say, args=({random.choice(bufor)},)
            ).start()

        elif keywords[7] in query:  # * 7 spotify
            bufor = text[7].split("&")
            if which("spotify.exe") == None:
                multiprocessing.Process(target=speak.say, args=({bufor[1]},)).start()
            else:
                multiprocessing.Process(target=speak.say, args=({bufor[0]},)).start()
                subprocess.call(["spotify.exe"])

        elif keywords[8] in query:  # * 8 maps
            multiprocessing.Process(target=speak.say, args=(text[8],)).start()
            webbrowser.open("www.google.pl/maps")

        elif keywords[9] in query:  # * 9 thanks
            multiprocessing.Process(target=speak.say, args=(text[9],)).start()

        elif keywords[10] in query:  # * 10 what is your name?
            multiprocessing.Process(target=speak.say, args=(text[10],)).start()

        elif keywords[11] in query:  # * 11 where is
            query = query.replace(keywords[11], "")
            multiprocessing.Process(
                target=speak.say, args=(f"{text[11]}{query}",)
            ).start()
            webbrowser.open("https://www.google.pl/maps/place/" + query + "")

        elif keywords[12] in query:  # * 12 search
            webbrowser.open("" + query.replace(keywords[12], "") + "")
