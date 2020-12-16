import env
from datetime import datetime, timedelta
from apple_calendar_integration import ICloudCalendarAPI
api = ICloudCalendarAPI(env.IcloudUsername, env.IcouldPassword)

def createAppleCalendarEvent(datetime, title):
        
        return True