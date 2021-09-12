import datetime
import json
import os
import random
from time import sleep
import requests


def main():
    location_ids = list(map(int, os.getenv('LOCATION_IDS').split(',')))
    with open('global-entry.json') as stream:
        locations = {location['id']: location for location in json.load(stream)}
    print(f'Searching for appointments at {", ".join([locations[location_id]["shortName"] for location_id in location_ids])}')
    while True:
        for location_id in location_ids:
            appointment = requests.get(f'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={location_id}&minimum=1').json()
            if appointment:
                appointment = appointment[0]
                print(f'Appointment found: {appointment}')
                appointment_datetime = datetime.datetime.strptime(appointment['startTimestamp'], r'%Y-%m-%dT%H:%M')

                if os.getenv('IFTTT_WEBHOOK_URL'):
                    requests.post(os.getenv('IFTTT_WEBHOOK_URL'), json={'value1': locations[location_id]['shortName'], 'value2': appointment_datetime.strftime(r'%A, %B %d, %Y at %H:%M')})
            else:
                print(f'No appointments found at {locations[location_id]["shortName"]}')
        rand = random.randint(30, 90)
        print(f'Sleeping for {rand} seconds')
        sleep(rand)


if __name__ == "__main__":
    main()
