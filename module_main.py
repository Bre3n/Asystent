import asyncio
import json
import os
import random
import threading
from datetime import datetime
from os import listdir
from os.path import isfile, join

import speech_recognition as sr

import main
import settings
import speak

r = sr.Recognizer()


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


def getThreadByName(name):
    threads = threading.enumerate()  # Threads list
    for thread in threads:
        if thread.name == name:
            return thread


async def change_username(bufor, language):
    x = threading.Thread(target=speak.say, args=({bufor[0]},))
    x.start()
    await asyncio.sleep(2)
    query = takeCommand(language)
    settings.create_settings(query, language)
    x = threading.Thread(target=speak.say, args=(f"{bufor[1]} {query}",)).start()
