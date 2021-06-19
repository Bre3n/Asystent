import os
import random
import threading

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
user_name = "Mateusz"


def welcome():
    engine.say(f"Good morning {user_name}")
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()


def say(audio):
    engine.say(audio)
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()
