import json
import os
def create_init():
    data = {}
    data["settings"] = []
    data["settings"] = [
        {"language": "en-en"},
    ]

    text = {}
    text["text"] = []
    text["text"] = [
        {"language": "pl"},
    ]

    with open("settings.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
    if os.path.isdir("language")== False:
        os.mkdir("language")
    with open("language/pl-pl.json", "w") as write_file:
        json.dump(text, write_file, indent=4)

    with open("settings.json") as json_file:
        data = json.load(json_file)
        for p in data["settings"]:
            print(f'language: {p["language"]}')
            print("")
