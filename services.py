import speech_recognition as sr
import wolframalpha
import wikipedia
import pyttsx3
import env
app_id = env.appid
client = wolframalpha.Client(app_id)
engine = pyttsx3.init()
r = sr.Recognizer()
def speakText(command):
        print(command)
        engine.say(""+command)
        engine.runAndWait()

def oscarIsListening(counter, sorryText, user):
        if (counter == 0):
                speakText("Hi, "+user+" What is your name?")
        with sr.Microphone() as source:
                if (source is not None):
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        counter = 1
                        return MyText, counter
                else:
                        speakText(sorryText)
                        return None, counter

def createDir(location):
        if _platform == "linux" or _platform == "linux2":
                # linux
                pass
        elif _platform == "darwin":
                # MAC OS X
                
        elif _platform == "win32":
                # Windows
                pass
        elif _platform == "win64":
                # Windows 64-bit
                pass
        else:
                pass

def oscarIsOnlyListening(sorryText):
        with sr.Microphone() as source:
                if (source is not None):
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        data = int(''.join(format(ord(i), 'b') for i in MyText))
                        return data
                else:
                        speakText(sorryText)
                        return None