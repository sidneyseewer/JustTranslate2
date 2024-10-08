
from functions import *

lan = [
    ('de', 'Deutsch'),
    ('fr', 'Français'),
    ('es', 'Espanol'),
    ('ru', 'Russki')
    ]
app_name = "JustTranslate"

def demo():
    translator = Translator(lan[0][0])
    print("Text: ", translator.translate("Good Morning"))

if __name__ == "__main__":
    demo()