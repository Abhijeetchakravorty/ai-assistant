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
try:
        _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
counter = 0
try:
        data, counter = services.oscarIsListening(counter, sorryText, user)
        if (data is not None):
                services.speakText("Hi "+data+"! Is that correct?")
                if (counter != 0):
                        user = data
                        confirm, counter = services.oscarIsListening(counter, sorryText, None)
                        print("I am here")
                        confirmRcvd = int(''.join(format(ord(i), 'b') for i in "yes"))
                        confirm = int(''.join(format(ord(i), 'b') for i in confirm))
                        if (confirm == confirmRcvd):
                                services.speakText("Okay "+user+", here are the list of things which I can do. Please choose anyone one of them")
                                services.speakText(""" 
                                        1. Create calendar events \n
                                        2. Play some music \n
                                        3. Open a website with a url \n
                                        4. Open a game \n
                                        5. Crawl some data \n
                                        6. Create a basic website
                                """)
                                
                                services.speakText(user+" please choose an option")
                                option = services.oscarIsOnlyListening(sorryText)
                                print("Option is printed: "+option)
                                if (option == 110001):
                                        services.speakText("Please provide the time for setting the event: ")
                                        datetime = services.oscarIsOnlyListening()
                                        services.speakText("Please provide a title for the event.")
                                        title = services.oscarIsOnlyListening()
                                        services.speakText("For how long the event should last?")
                                        print(datetime)
                                        print(title)
                        else:
                                counter = 0
        else:
                user = "user!"
                counter = 0
except:
        user = "user!"
        counter = 0
        services.speakText(sorryText)
       

# while(True):
#         try:
#                 services.speakText("Okay "+user+", here are the list of things which I can do. Please choose anyone one of them")
#                 services.speakText(""" 
#                         1. Create calendar events \n
#                         2. Play some music \n
#                         3. Open a website with a url \n
#                         4. Open a game \n
#                         5. Crawl some data \n
#                         6. Create a basic website
#                 """)
                
#                 services.speakText(user+" please choose an option")
#                 option = services.oscarIsOnlyListening(sorryText)
#                 print("Option is printed: "+option)
#                 if (option == 110001):
#                         ostype = services.returnTypeOfOs()
#                         if (ostype == "osx"):
#                                 services.speakText("Please provide the time for setting the event: ")
#                                 datetime = services.oscarIsOnlyListening()
#                                 services.speakText("Please provide a title for the event.")
#                                 title = services.oscarIsOnlyListening()
#                                 services.speakText("For how long the event should last?")
#                                 print(datetime)
#                                 print(title)
#                                 # osx.createAppleCalendarEvent()
#                 elif (option == 111010011101111101111):
#                         pass
#                 elif (option == 11101001101000111001011001011100101):
#                         pass
#                 elif (option == 1100110110111111101011110010):
#                         pass
#                 elif (option == 1100110110100111101101100101):
#                         pass
#                 elif (option == 111001111010011111000):
#                         pass
#                 else:
#                         print("Could not find a matching option")
#                         break
#         except:
#                 pass
