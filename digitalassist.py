import env
import wolframalpha
import wikipedia
import pyttsx3
import ssl
import PySimpleGUI as sg
import speech_recognition as sr
app_id = env.appid
try:
        _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
print("App Id: "+app_id)
client = wolframalpha.Client(app_id)
engine = pyttsx3.init()
r = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def speakText(command):
        print(command)
        engine.say(""+command)
        engine.runAndWait()

def findWikiResult(question):
        wiki_res = wikipedia.summary(question, sentences=1)
        speakText(wiki_res)

def findWolframResult(question):
        res = client.query(question)
        wolfram_res = next(res.results).text
        speakText(wolfram_res)

while(1):
        try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        print("Did you say: "+MyText)
                        try:
                                findWolframResult(MyText)
                        except:
                                print("Couldn't fetch wolfram results")
                        try:
                                findWikiResult(MyText)
                        except:
                                print("Exception occurred")

        except sr.RequestError as er:
                print("Could not request results {0}".format(er))
        except sr.UnknownValueError:
                print("unknown error occured")