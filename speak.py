import json
import os
import random
import threading

import pyttsx3

text_list = []

with open("settings.json") as json_file:
    data = json.load(json_file)
    for p in data["settings"]:
        lang = p["language"]
        username = p["username"]
with open(f"languages/{lang}.json") as json_file:
    data = json.load(json_file)
    for p in data["text"]:
        text_list.append(p["1"])
if lang == "en-en":
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
elif lang == "pl-pl":
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)


def welcome():
    engine.say(f"{text_list[0]} {username}")
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()


def say(audio):
    engine.say(audio)
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()
