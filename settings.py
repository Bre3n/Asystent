import json
import os


def check_file():
    if os.path.exists("settings.json") == False:
        create_settings("", "pl-pl")
    if os.path.isdir("languages") == False:
        os.mkdir("languages")
    if os.path.exists("languages/pl-pl.json") == False:
        create_language("pl-pl")
    if os.path.exists("languages/en-en.json") == False:
        create_language("en-en")


def create_settings(var, lang):
    data = {}
    data["settings"] = []
    data["settings"] = [
        {"language": f"{lang}", "username": f"{var}"},
    ]

    with open("settings.json", "w") as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)


def create_language(var):
    text = {}
    text["keywords"] = []
    if var == "pl-pl":
        text["keywords"] = [
            {
                "1": "dzień dobry",
                "2": "cześć",
                "3": "zmień moje imię",
                "4": "jaka jest godzina",
                "5": "jaki jest dzisiaj dzień",
                "6": "ok google",
                "7": "alexa",
                "8": "włącz spotify",
                "9": "włącz mapy",
            }
        ]
        text["text"] = []
        text["text"] = [
            {
                "1": "Dzień dobry",
                "2": "cześć, jak się dzisiaj miewasz?",
                "3": "jasne, powiedz jak mam do ciebie mówić&Miło mi ciebie poznać",
                "4": "jest godzina",
                "5": "dzisiaj jest",
                "6": "hmmm, chyba pomyliłeś asystentów&naprawdę?",
                "7": "hmmm, chyba pomyliłeś asystentów&naprawdę?",
                "8": "miłego słuchania&spotify nie jest zainstalowane",
                "9": "szerokiej drogi!",
            },
        ]
    elif var == "en-en":
        text["keywords"] = [
            {
                "1": "good morning",
                "2": "hello",
                "3": "change my name",
                "4": "what time is it",
                "5": "what day is today",
                "6": "ok google",
                "7": "alexa",
                "8": "turn on spotify",
                "9": "turn on maps",
            }
        ]
        text["text"] = []
        text["text"] = [
            {
                "1": "good morning",
                "2": "Hello, how you doing today",
                "3": "alright, just say your new name&Nice to meet you",
                "4": "it is",
                "5": "it is",
                "6": "hmmm, i think you've got the wrong assistant&really?",
                "7": "hmmm, i think you've got the wrong assistant&really?",
                "8": "enjoy listening!&spotify is not installed",
                "9": "enjoy driving",
            },
        ]
    with open(f"languages/{var}.json", "w") as write_file:
        json.dump(text, write_file, indent=4, ensure_ascii=False)
    text = {}


if __name__ == "__main__":
    check_file()
