from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from app.models import Appreq
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None
parentdir = os.path.join(os.path.dirname(__file__),"client_secrets.json")
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = parentdir
APPLICATION_NAME = 'Test1'
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
def main(request):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar' , 'v3' , http=http)
        t = request.session['ID']
        evnt = Appreq.objects.filter(ID__in=t).values_list('event_id')
        event_id = evnt[0]
        service.events().delete(calendarId='primary', eventId='%s' %event_id).execute()
if __name__ == '__main__' :
        main()
