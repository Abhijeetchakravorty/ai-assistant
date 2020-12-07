import env
import wolframalpha
import wikipedia
import pyttsx3
import ssl
import PySimpleGUI as sg
import speech_recognition as sr
app_id = env.appid
ssl.create_default_context = ssl._create_unverified_context
client = wolframalpha.Client(app_id)
engine = pyttsx3.init()
r = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def speakText(command):
        print(command)
        engine.say(""+command)
        engine.runAndWait()

while(1):
        try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        print("Did you say: "+MyText)
                        speakText(MyText)
        except sr.RequestError as er:
                print("Could not request results {0}".format(er))
        except sr.UnknownValueError:
                print("unknown error occured")