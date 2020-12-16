from datetime import datetime
import env
import ssl
import os
from pathlib import Path
import services
import osx
try:
        _create_unverified_https_context = ssl._crate_unverified_context
except AttributeError:
        pass
else:
        ssl._create_default_https_context = _create_unverified_https_context
        #  2. Play some music \n
        #                                 3. Open a website with a url \n
        #                                 4. Open a game \n
        #                                 5. Crawl some data \n
        #                                 6. Create a basic website \n

services.speakText("""Welcome! I am Oscar. Your personal assistant""")
services.speakText("""I can perform some small tasks like
                                        1. Create calendar events \n
                                       
                                        
                What would you like me to do?""")
data = int(input("Enter choice: "))

if (data == 1):
        if (services.returnTypeOfOs() == "osx"):
                services.speakText("Please enter the date and time on which you would like to set the event")
                #date input
                services.speakText("Enter the year")
                year = int(input("Enter year: "))
                services.speakText("Enter the month")
                month = int(input("Enter month: "))
                services.speakText("Enter date")
                dt = int(input("Enter date only: "))
                
                #time input
                services.speakText("Enter hour")
                hour = int(input("Enter hour: "))

                services.speakText("Enter minutes")
                mints = int(input("Enter minutes: "))

                services.speakText("Enter seconds")
                sec = int(input("Enter seconds"))

                fulltime = ""+str(year)+"-"+str(month)+"-"+str(dt)+" "+str(hour)+":"+str(mints)+":"+str(sec)+".000000"
                print(fulltime)
                string = datetime.datetime.strptime(fulltime, "%Y-%m-%d %H:%M:%S.%f")
                print(string)
                timestamp = datetime.fromtimestamp(string)
                print(timestamp)
        else:
                print("Incompatible OS detected")