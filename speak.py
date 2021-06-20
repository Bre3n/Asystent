import json
import os
import threading

import pyttsx3

import settings

if os.path.exists("settings.json") == False:
    settings.check_file()
with open("settings.json") as json_file:
    data = json.load(json_file)
    for p in data["settings"]:
        lang = p["language"]
        username = p["username"]
if lang == "en-en":
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
elif lang == "pl-pl":
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)


def welcome(var):
    engine.say(f"{var} {username}")
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()


def say(audio):
    if engine._inLoop:
        engine.endLoop()
    engine.say(audio)
    engine.runAndWait()
