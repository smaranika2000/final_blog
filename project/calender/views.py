from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
from app1.models import confApt
from app1.forms import Appointment

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)

credentials = pickle.load(open("token.pkl", "rb"))
print(credentials)
service = build("calendar", "v3", credentials=credentials)
print(credentials)
result = service.calendarList().list().execute()


# get my calendar event
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id).execute()
#print (result)


#create a new calendar Events

# start_time = datetime(2021, 7, 25, 14, 0, 0)
# end_time = start_time + timedelta(hours=3)
# timezone = 'Asia/Kolkata'
# event = {
#   'summary': 'IPL Final 2019',
#   'location': 'Hyderabad',
#   'description': 'MI vs TBD',
#   'start': {
#     'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': timezone,
#   },
#   'end': {
#     'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': timezone,
#   },
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }
# print(service.events().insert(calendarId=calendar_id, body=event).execute())



#create a new calendar Events
import datefinder
# matches = datefinder.find_dates("5 may 9 PM")
# print(list(matches))


def bookApt(request):
    form=Appointment(auto_id=True)
    context = {'form':form}

    if request.method=="POST":
        required_specialist=request.POST['required_specialist']
        apointment_date=request.POST['apointment_date']
        global appointment_stime
        appointment_stime=request.POST['appointment_stime']
        confapt=confApt(
                required_specialist=required_specialist,
                apointment_date=apointment_date,
                appointment_stime=appointment_stime, 
        )
        confapt.save()
        messages.success(request, "Your post has been successfully sent")
        print(appointment_stime)
        time= str(apointment_date)+" "+str(appointment_stime)
        
        create_event(time, "Appointment")
        create_event1(time, "Appointment")
    return render(request,'bookapt.html',context)
    

def create_event(start_time_str, summary, duration=0.75, description=None, location=None):
    
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()

def bookapt1(request):
    return render(request,"bookApt1.html")


flow1 = InstalledAppFlow.from_client_secrets_file("client_secret1.json", scopes=scopes)

# credentials1 = flow.run_console()
# print(credentials1)

# pickle.dump(credentials1,open("token1.pkl","wb"))
credentials1 = pickle.load(open("token1.pkl","rb"))
print(credentials1)

service1 = build("calendar", "v3", credentials=credentials1)

result1 = service1.calendarList().list().execute()
print(result1)
print(result1['items'][0])

calendar_id1 = result1['items'][0]['id']
result1 = service1.events().list(calendarId=calendar_id1).execute()


import datefinder
def create_event1(start_time_str, summary, duration=0.75, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service1.events().insert(calendarId='primary', body=event).execute()

