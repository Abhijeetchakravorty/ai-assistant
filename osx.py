import env
from datetime import datetime, timedelta
from apple_calendar_integration import ICloudCalendarAPI
api = ICloudCalendarAPI(env.IcloudUsername, env.IcouldPassword)

def createAppleCalendarEvent(start_date, end_date, title):
        etag, ctag, guid = api.create_event(title, start_date, end_date)
        print(etag)
        print(ctag)
        print(guid)