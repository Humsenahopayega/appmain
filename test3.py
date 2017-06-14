from __future__ import print_function
from django.core import serializers
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from app.models import Appreq
import datetime

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: 
            credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
    return credentials


def main() :
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        CAL = discovery.build('calendar' , 'v3' , http=http)
        summary = serializers.serialize('json' ,Appreq.objects.filter( title='Dinner').values('title'))
        EVENT = {
                'summary' : summary['title'] ,
                'start' : { 'dateTime' : '2017-06-08T15:00:00+05:30'},
                'end' : { 'dateTime' : '2017-06-08T17:00:00+05:30'}
                }
        event = CAL.events().insert(calendarId='primary', body=EVENT).execute()
        print ('Event created: %s' % (event.get('htmlLink')))
if __name__ == '__main__' :
        main()
