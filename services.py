from sys import platform as _platform
import speech_recognition as sr
import wolframalpha
import wikipedia
import pyttsx3
import env
from datetime import datetime
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
                
def currIsSelected(givendate, month, year):
        givendate = int(givendate)
        month = int(month)
        year = int(year)
        currDt = datetime.now()
        if (currDt.year == year and currDt.month == month and currDt.day == givendate):
                return True
        else:
                return False
        
def currTime():
        now = datetime.now()
        currTime = now.strftime("%H:%M:%S")
        currTime = currTime.split(":")
        print(currTime)




