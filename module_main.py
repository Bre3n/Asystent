import asyncio
import json
import multiprocessing
import os
import random
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


async def change_username(bufor, language):
    multiprocessing.Process(target=speak.say, args=({bufor[0]},)).start()
    while True:
        await asyncio.sleep(3)
        query = takeCommand(language)
        if query != "None":
            settings.create_settings(query, language)
            multiprocessing.Process(
                target=speak.say, args=(f"{bufor[1]} {query}. {bufor[2]}",)
            ).start()
            return 0
        else:
            multiprocessing.Process(target=speak.say, args=(f"{bufor[3]}",)).start()
