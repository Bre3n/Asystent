import json
import os
import random
import threading

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
user_name = "Mateusz"

with open("settings.json") as json_file:
    data = json.load(json_file)
    print(data["settings"])
    for p in data["settings"]:
        lang = p["language"]
with open(f"languages/{lang}.json") as json_file:
    data = json.load(json_file)
    for p in data["text"]:
        greetings = p["greetings"]


def welcome():
    engine.say(f"{greetings} {user_name}")
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()


def say(audio):
    engine.say(audio)
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()
