import os

import pyttsx3
import threading
import random

engine = pyttsx3.init()
engine.setProperty('rate', 150)
user_name = "Mateusz"

def welcome():
    engine.say(f"Dzień dobry {user_name}")
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()
    
def say(audio):
    engine.say(audio)
    if engine._inLoop:
        engine.endLoop()
    engine.runAndWait()