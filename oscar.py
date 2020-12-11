import env
import ssl
from sys import platform as _platform
import os
import appscript
import services
sorryText = "I am sorry! I couldn't hear your name. Could you please try again?"
user = "User!"
try:
        _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
counter = 0
while(True):
        try:
                data, counter = services.oscarIsListening(counter, sorryText, user)
                if (data is not None):
                        services.speakText("Hi "+data+"! Is that correct?")
                        if (counter != 0):
                                user = data
                                confirm, counter = services.oscarIsListening(counter, sorryText, None)
                                confirmRcvd = int(''.join(format(ord(i), 'b') for i in "yes"))
                                confirm = int(''.join(format(ord(i), 'b') for i in confirm))
                                path = os.getcwd()+"/oscar/setup"
                                if (confirm == confirmRcvd):
                                        os.mkdir(path+env.apiDirName)
                                        i = open(path+env.apiDirName+"/"+env.directoryInIt, "w+")
                                        s = open(path+env.apiDirName+"/"+env.serializerInIt, "w+")
                                        v = open(path+env.apiDirName+"/"+env.viewsInIt, "w+")
                                        u = open(path+env.apiDirName+"/"+env.urlInIt, "w+")
                                        break
                                else:
                                        counter = 0
                else:
                        user = "user!"
                        counter = 0
        except:
                user = "user!"
                counter = 0
                services.speakText(sorryText)

while(True):
        try:
                services.speakText("Okay "+user+", here are the list of things which I can do. Please choose anyone one of them")
                services.speakText(""" 
                        1. Create calendar events \n
                        2. Play some music \n
                        3. Open a website with a url \n
                        4. Open a game \n
                        5. Crawl some data \n
                        6. Create a basic website
                """)
                services.speakText("So "+user+", what can I do for you?")
        except:
                pass
