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
                x = datetime.now()
                services.speakText("Please enter the date and time on which you would like to set the event")
                #date input
                services.speakText("Enter the year")
                while(True):
                        year = int(input("Enter year: "))
                        if (year < x.year):
                                services.speakText("Please enter a current or future year")
                        else:
                                break
                
                while(True):
                        services.speakText("Enter the month")
                        month = int(input("Enter month: "))
                        if (month < x.month):
                                services.speakText("Please choose a future month or current month")
                        else:
                                if (month < 10):
                                        month = "0"+str(month)
                                break

                while(True):
                        services.speakText("Enter date only")
                        dt = int(input("Enter date only: "))
                        if (dt < x.day):
                                services.speakText("Please enter a future date")
                        else:
                                if (dt < 10):
                                        dt = "0"+str(dt)
                                break

                while(True):
                        services.speakText("Enter hour")
                        hour = int(input("Enter hour: "))
                        #time input
                        if(services.currIsSelected(dt, month, year)):
                                currTime = services.currTime()[0]
                                print(currTime)
                                # for i in range(len(currTime)):
                                #         if (int(i) < hour and int(i)):

                                break
                        else:
                                break
                        
                

                services.speakText("Enter minutes")
                mints = int(input("Enter minutes: "))
                
                if (mints < 10):
                        mints = "0"+str(mints)

                services.speakText("Enter seconds")
                sec = int(input("Enter seconds"))
                if (sec < 10):
                        sec = "0"+str(sec)

                fulltime = ""+str(year)+"-"+str(month)+"-"+str(dt)+" "+str(hour)+":"+str(mints)+":"+str(sec)+".000000"
                print(fulltime)
                string = datetime.fromisoformat(fulltime)
                print(string)
        else:
                print("Incompatible OS detected")