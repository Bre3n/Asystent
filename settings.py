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
                "0": "dzień dobry",
                "1": "cześć",
                "2": "zmień moje imię",
                "3": "jaka jest godzina",
                "4": "jaki jest dzisiaj dzień",
                "5": "ok google",
                "6": "alexa",
                "7": "włącz spotify",
                "8": "włącz mapy",
                "9": "dzięki",
                "10": "jak masz na imię",
                "11": "gdzie jest",
                "12": "wyszukaj",
            }
        ]
        text["text"] = []
        text["text"] = [
            {
                "0": "Dzień dobry",
                "1": "cześć, jak się dzisiaj miewasz?",
                "2": "powiedz jak mam do ciebie mówić&Miło mi ciebie poznać&Co chcesz abym dla ciebie zrobiła?&powtórz proszę",
                "3": "jest godzina",
                "4": "dzisiaj jest",
                "5": "hmmm, chyba pomyliłeś asystentów&naprawdę?",
                "6": "hmmm, chyba pomyliłeś asystentów&naprawdę?",
                "7": "miłego słuchania&spotify nie jest zainstalowane",
                "8": "szerokiej drogi!",
                "9": "nie ma za co",
                "10": "przyjaciele mówią do mnie Sofia",
                "11": "otwieram lokalizacje",
                "12": "",
            },
        ]
    elif var == "en-en":
        text["keywords"] = [
            {
                "0": "good morning",
                "1": "hello",
                "2": "change my name",
                "3": "what time is it",
                "4": "what day is today",
                "5": "ok google",
                "6": "alexa",
                "7": "turn on spotify",
                "8": "turn on maps",
                "9": "thanks",
                "10": "what is your name",
                "11": "where is",
                "12": "search",
            }
        ]
        text["text"] = []
        text["text"] = [
            {
                "0": "good morning",
                "1": "Hello, how you doing today",
                "2": "please say your name&Nice to meet you&what do you want to do today&sorry repeat please",
                "3": "it is",
                "4": "it is",
                "5": "hmmm, i think you've got the wrong assistant&really?",
                "6": "hmmm, i think you've got the wrong assistant&really?",
                "7": "enjoy listening!&spotify is not installed",
                "8": "enjoy driving",
                "9": "you are welcome",
                "10": "my friends call me Sofia",
                "11": "opening localisation",
                "12": "",
            },
        ]
    with open(f"languages/{var}.json", "w") as write_file:
        json.dump(text, write_file, indent=4, ensure_ascii=False)
    text = {}


if __name__ == "__main__":
    check_file()
