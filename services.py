from sys import platform as _platform
import speech_recognition as sr
import wolframalpha
import wikipedia
import pyttsx3
import env
from datetime import datetime
from datetime import timedelta
app_id = env.appid
client = wolframalpha.Client(app_id)
engine = pyttsx3.init()
def speakText(command):
        print(command)
        engine.say(""+command)
        engine.runAndWait()

def createDir(location):
        if _platform == "linux" or _platform == "linux2":
                # linux
                pass
        elif _platform == "darwin":
                # MAC OS X
                pass
        elif _platform == "win32":
                # Windows
                pass
        elif _platform == "win64":
                # Windows 64-bit
                pass
        else:
                pass

def returnTypeOfOs():
        if _platform == "linux" or _platform == "linux2":
                # linux
                return "linux"
        elif _platform == "darwin":
                # MAC OS X
                return "osx"
        elif _platform == "win32":
                # Windows
                return "windows32"
        elif _platform == "win64":
                # Windows 64-bit
                return "windows64"
        else:
                pass

def oscarIsListening(counter, sorryText, user):
        r = sr.Recognizer()
        if (counter == 0):
                speakText("Hi, "+user+" What is your name?")
        with sr.Microphone() as source:
                if (source is not None):
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        counter = 1
                        print(MyText)
                        return MyText, counter
                else:
                        speakText(sorryText)
                        return None, counter

def oscarIsOnlyListening(sorryText):
        r = sr.Recognizer()
        with sr.Microphone() as source:
                if (source is not None):
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        return MyText
                else:
                        speakText(sorryText)
                        return None
        
def currTimeStamp():
        now = datetime.now()
        ts = now.timestamp()
        return ts


def add_hours(time_string, hr):
        updated = ( time_string + timedelta( hours=hr )).strftime('%Y-%m-%d %H:%M:%S.%f')
        print(updated)
        return updated