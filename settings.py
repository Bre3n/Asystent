import json
import os


def check_file():
    if os.path.exists("settings.json") == False:
        create_settings()
    if os.path.isdir("languages") == False:
        os.mkdir("languages")
    if os.path.exists("pl-pl.json") == False or os.path.exists("en-en.json"):
        create_language()


def create_settings():
    data = {}
    data["settings"] = []
    data["settings"] = [
        {"language": "en-en", "username": ""},
    ]

    with open("settings.json", "w") as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)


def create_language():
    text = {}
    text["text"] = []
    text["text"] = [
        {"greetings": "Dzień dobry"},
    ]

    with open("languages/pl-pl.json", "w") as write_file:
        json.dump(text, write_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    check_file()
