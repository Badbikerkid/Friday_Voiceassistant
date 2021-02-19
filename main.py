import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import random
import pywhatkit
import wikipedia
import webbrowser
import time
from translate import Translator
from gtts import gTTS
import os
import wolframalpha
import pyautogui
from pyfiglet import Figlet
from datetime import date


# function defined for forming a pattern 'FRIDAY'
def friday():
    text = Figlet(font='digital')
    print(text.renderText("FRIDAY"))


# for mac users remove 'sapi5' from init on line 24
engine = pyttsx3.init('sapi5')


# command intake
def take(text):
    engine.say(text)
    engine.runAndWait()


# wish_me is used for wishing the user (eg. good-morning/afternoon/evening)
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        take("Good Morning Sir !")

    elif 12 <= hour < 18:
        take("Good Afternoon Sir !")

    else:
        take("Good Evening Sir !")

    assistant_name = "Friday 1 point o"
    take("I am your Assistant")
    take(assistant_name)
    take("How may i help you")


# command intake
def talk(command_intake):
    engine.say(command_intake)
    engine.runAndWait()


# take voice input from user through mic and convert voice to string using pyttsx3
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        command_user = listener.recognize_google(voice, language='en-in')
        command_user = command_user.lower()

    except Exception:
        print("Say the command again")
        return "None"
    return command_user


if __name__ == "__main__":
    friday()
    wish_me()
    while True:
        command = take_command()

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            print("Listen to{} till then i'll sleep for a few seconds".format(song))
            talk("Listen to {} till then i'll sleep for a few seconds".format(song))
            pywhatkit.playonyt(song)
            time.sleep(10)
            talk('I am awake sir!')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H %M %p')
            print(time)
            talk("Current time is" + time)

        elif 'date' in command:
            date = date.today()
            print(date)
            talk(date)

        elif 'who is' in command:
            person = command.replace("who is", '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'roll a dice' in command:
            choices = [1, 2, 3, 4, 5, 6]
            output = random.choice(choices)
            print(output)
            talk("The output is {}".format(output))

        elif 'flip a coin' in command:
            choices = ['Tails', 'Heads']
            output = random.choice(choices)
            print(output)
            talk("The outcome is" + output)

        elif 'are you single' in command:
            talk("sorry i have a girlfriend")
            print("Sorry I Have a girlfriend")

        elif "will you go on a date with me" in command:
            print("Sorry I am not feeling well")
            talk("Sorry i am not feeling well")

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
            time.sleep(6)

        elif 'open google' in command:
            webbrowser.open("google.com")
            time.sleep(6)

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")
            time.sleep(6)

        elif 'how are you' in command:
            print("I am fine. Thank you")
            talk("I am fine. Thank you")
            print("How are you?")
            talk("How are you?")

        elif "who created you" in command:
            print("I was created by JV2S")
            talk("I was created by JV2S")

        elif 'who am i' in command:
            print("If you are talking and giving me commands then you are definitely human")
            talk("If you are talking and giving me commands then you are definitely human")

        elif "why did you come to this world" in command:
            print("Well, this is a secret I am not willing to tell")
            talk("Well, this is a secret i am not willing to tell")

        elif "hello testing 123" in command:
            print("I am completely operational and all my circuits are working properly")
            talk("I am completely operational and all my circuits are working properly")

        elif "can i call you jarvis" in command:
            print("I think you have mistaken me for another intelligent assistant")
            talk("I think you have mistaken me for another intelligent assistant")
            print('Mr Stark is that you?')
            talk('Mr Stark is that you?')

        elif 'can you dance with me' in command:
            print("No these guilty feet have got no rhythm, Wait i have no feet")
            talk("No these guilty feet have got no rhythm, Wait i have no feet")

        elif "when will the world end" in command:
            print('''Well,Unix 32-bit time overflows...
                        ...on January 19, 2038. Maybe then!''')
            talk("Well,Unix 32-bit time overflows on January 19,2038.Maybe then,")

        elif 'how much wood would a woodchuck chuck if a woodchuck could chuck chuck wood' in command:
            talk("42?,That cant be right")
            print("42?,That cant be right")
            talk("How about another tongue twister")
            print("How about another tongue twister")
            take_command()
            if 'ok' in command:
                talk("""Peter Piper picked a peck of pickled pepper
                A peck of pickled peppers Peter Piper picked
                If Peter Piper picked a peck of pickled peppers
                Where’s the peck of pickled peppers Peter Piper picked?""")
                print("""Peter Piper picked a peck of pickled pepper
                A peck of pickled peppers Peter Piper picked
                If Peter Piper picked a peck of pickled peppers
                Where’s the peck of pickled peppers Peter Piper picked? """)
            else:
                print("Ok next time")
                talk("Ok next time")

        elif "exit" in command:
            print("Thanks for giving me your time")
            talk('Thanks for giving me your time')
            exit()

        elif "quit" in command:
            print("Thanks for giving me your time")
            talk('Thanks for giving me your time')
            exit()

        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            print("User asked to locate")
            talk("User asked to Locate")
            print(location.upper())
            talk(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + command + "")
            time.sleep(8)

        elif "translate" in command:
            command = command.replace("translate", "")
            print("Which language do you want to translate in ?")
            talk("Which language do you want to translate in ?")
            command1 = take_command()

            if "german" in command1:
                translator = Translator(to_lang="German")
                translation = translator.translate(command)
                obs = gTTS(text=translation, lang='de', slow=False)
                obs.save('german.mp3')
                print("In German{} is {}".format(command, translation))
                talk("In German" + command + "is")
                os.system('german.mp3')
                time.sleep(3)

            elif 'french' in command1:
                translator = Translator(to_lang="French")
                translation = translator.translate(command)
                obs1 = gTTS(text=translation, lang='fr', slow=False)
                obs1.save("french.mp3")
                print("In French{} is {}".format(command, translation))
                talk("In French" + command + "is")
                os.system('french.mp3')
                time.sleep(3)

            elif 'italian' in command1:
                translator = Translator(to_lang="Italian")
                translation = translator.translate(command)
                obs2 = gTTS(text=translation, lang='it', slow=False)
                obs2.save("italian.mp3")
                print("In Italian{} is {}".format(command, translation))
                talk("In Italian" + command + "is")
                os.system('italian.mp3')
                time.sleep(3)

            elif 'russian' in command1:
                translator = Translator(to_lang="Russian")
                translation = translator.translate(command)
                my = gTTS(text=translation, lang='ru', slow=False)
                my.save("russia.mp3")
                print("In Russian{} is {}".format(command, translation))
                talk("In Russian" + command + "is")
                os.system('russia.mp3')
                time.sleep(3)

            elif "japanese" in command1:
                translator = Translator(to_lang="Japanese")
                translation = translator.translate(command)
                my1 = gTTS(text=translation, lang='ja', slow=False)
                my1.save("japanese.mp3")
                print("In Japanese{} is {}".format(command, translation))
                talk("In Japanese" + command + "is")
                os.system('japanese.mp3')
                time.sleep(3)

            elif "hindi" in command1:
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(command)
                my_object = gTTS(text=translation, lang='hi', slow=False)
                my_object.save("welcome.mp3")
                print("In Hindi{} is {}".format(command, translation))
                talk("In Hindi" + command + "is")
                os.system("welcome.mp3")
                time.sleep(3)

        elif 'screenshot' in command:
            time.sleep(3)
            print('Taking SS now!')
            talk('Taking screenshot now')
            screenshot = pyautogui.screenshot()
            screenshot.save("screen.png")
            print('Done!')
            talk('Done')

        elif 'friday' in command:
            wish_me()

        elif "calculate" in command:
            question = command
            command = command.replace("calculate", "")
            client = wolframalpha.Client('Q25UJH-7HU99AVT32')
            res = client.query(question)
            answer = next(res.results).text
            print("The answer is " + answer)
            talk("The answer is " + answer)

        elif 'what is' in command:
            question = command
            command = command.replace('what is', "")
            client = wolframalpha.Client('Q25UJH-7HU99AVT32')
            res = client.query(question)
            answer = next(res.results).text
            print("The answer is " + answer)
            talk("The answer is " + answer)
