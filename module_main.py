import asyncio
import json
import os
import random
import threading
import time
from os import listdir
from os.path import isfile, join

import pyttsx3
import speech_recognition as sr

import main
import settings
import speak


async def change_username(bufor, language):
    x = threading.Thread(target=speak.say, args=({bufor[0]},))
    x.start()
    await asyncio.sleep(2)
    query = main.takeCommand(language)
    settings.create_settings(query, language)
    x = threading.Thread(target=speak.say, args=(f"{bufor[1]} {query}",))
    x.start()
