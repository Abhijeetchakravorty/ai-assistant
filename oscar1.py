from datetime import datetime, timedelta
import env
import ssl
import os
from pathlib import Path
import services
import osx
import tictactoe
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
                                        2. Open a website with a url \n
                                        3. Open a game \n
                                        
                What would you like me to do?""")
data = int(input("Enter choice: "))
sec = 00.000000
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
                        try:
                                services.speakText("Enter hour")
                                hour = int(input("Enter hour: "))
                                services.speakText("Enter minutes")
                                mints = int(input("Enter minutes: "))
                                fullTime = ""+str(year)+"-"+str(month)+"-"+str(dt)+" "+str(hour)+":"+str(mints)+":"+str(sec)
                                finalTime = datetime.strptime(fullTime, "%Y-%m-%d %H:%M:%S.%f")
                                startTimestamp = datetime.timestamp(finalTime)
                                services.speakText("Please provide a title for the event")
                                title = input("Title for the event: ")
                                services.speakText("PLease provide the duration of the event in hours")
                                duration = int(input("Please provide duration in hours: "))
                                endTimeString = datetime.strptime(services.add_hours(finalTime, duration), "%Y-%m-%d %H:%M:%S.%f")
                                endTimeStamp = datetime.timestamp(endTimeString)
                                if (services.currTimeStamp() < startTimestamp):
                                        osx.createAppleCalendarEvent(startTimestamp, endTimeStamp, title)
                                        break
                                else:
                                        services.speakText("Please provide a higher timing")
                        except:
                                print("Unable to get ctag")

        else:
                print("Incompatible OS detected")

elif (data==2):
        if (services.returnTypeOfOs() == "osx"):
                services.speakText("Please provide a website url")
                url = input("Url: ")
                print(url)
                osx.openNewTab(url)        
        else:
                print("Incompatible OS detected")
elif (data==3):
       tictactoe.startGame()
else:
        pass