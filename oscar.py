import env
import ssl
from sys import platform as _platform
import os
import appscript
from pathlib import Path
import services
import osx
sorryText = "I am sorry! I couldn't hear your name. Could you please try again?"
user = "User!"
file  = Path(os.getcwd()+"/"+env.projectName+"/"+env.projectName+"/"+env.urlInIt).read_text()
# print(file)
data = []
indexData = file.index("[")
print(indexData)
data.append(indexData+1)
print(data)
parts = [file[i:j] for i, j in zip(data, data[1:]+[None])]
print(parts)
url = "path('"+env.setupApiEndPoint+"', include('"+env.setupApiUrlWiring+"', '"+env.setupApiDef+"'))"
parts.insert(0, url)
print(parts)
# # file.seek(520)
# # print(file.tell())
# # print(file.readline())
# for line in file:
#         data = line.split("[")

# print(data)
        

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
                                        try:
                                                os.makedirs(path+env.apiDirName)
                                                i = open(path+env.apiDirName+"/"+env.directoryInIt, "w+")
                                                s = open(path+env.apiDirName+"/"+env.serializerInIt, "w+")
                                                v = open(path+env.apiDirName+"/"+env.viewsInIt, "w+")
                                                u = open(path+env.apiDirName+"/"+env.urlInIt, "w+")
                                                file  = open(os.getcwd()+"/"+env.projectName+"/"+env.projectName+"/"+env.urlInIt, "w")
                                                file.write("%s = %s\n" % ())
                                                break
                                        except OSError as e:
                                                print("Directory exists")
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
                        2. Play some music \n¡™™
                        3. Open a website with a url \n
                        4. Open a game \n
                        5. Crawl some data \n
                        6. Create a basic website
                """)
                
                services.speakText("So "+user+", what can I do for you? Please choose an option")
                option = services.oscarIsOnlyListening("I am sorry! I couldn't hear that")
                print(option)
                if (option == 110111111011101100101):
                        ostype = services.returnTypeOfOs()
                        if (ostype == "osx"):
                                services.speakText("Please provide the time for setting the event: ")
                                datetime = services.oscarIsOnlyListening()
                                services.speakText("Please provide a title for the event.")
                                title = services.oscarIsOnlyListening()
                                services.speakText("For how long the event should last?")
                                print(datetime)
                                print(title)
                                # osx.createAppleCalendarEvent()
                elif (option == 111010011101111101111):

                elif (option == 11101001101000111001011001011100101):

                elif (option == 1100110110111111101011110010):

                elif (option == 1100110110100111101101100101):

                elif (option == 111001111010011111000):

                else:
                        print("Could not find a matching option")
                        pass
                break
        except:
                pass
