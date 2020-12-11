import env
import wolframalpha
import wikipedia
import pyttsx3
import ssl
import speech_recognition as sr
import os
import appscript
sorryText = "I am sorry! I couldn't hear your name. Could you please try again?"
user = "User!"
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
counter = 0
def speakText(command):
        print(command)
        engine.say(""+command)
        engine.runAndWait()

def oscarIsListening(self):
        if (self.counter == 0):
                speakText("Hi, "+self.user+" What is your name?")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                if (source is not None):
                        audio = r.listen(source)
                        MyText = r.recognize_google(audio)
                        MyText = MyText.lower()
                        self.counter += 1
                        return MyText
                else:
                        speakText(sorryText)
                        return None


print(os.name)
# def createDir(self, location):
        
# while(1):
#         try:
#                 if (counter == 0):
#                         data = oscarIsListening(self)
#                         if (data is not None):
#                                 speakText("Did you say "+data+"?")
#                                 speakText("Please confirm "+data+"")
#                         else:
#                                 speakText(sorryText)
#                 else:
#                         confirmName = oscarIsListening(self)
#                         if (confirmName == "yes"):
#                                 createDir(self, env.apiDirName)
#                         else:
#                                 pass
#         except:
#                 speakText(sorryText)