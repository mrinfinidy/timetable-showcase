import requests
import json

def times_berlin_pankow(time, date, timetable):
    url = 'https://www.fahrplan.guru/api/haltestelle?city=berlin&date=' + date + '&dir=dep&name=berlin-pankow&state=berlin&time=' + time
    res = requests.get(url)
    res = json.loads(res.text)

    timetable.append(1) # indicate berlin-pankow station
    
    for i in range(5):
        berlin_pankow_entry = []
        berlin_pankow_entry.append(res["transports"][i]["nearest_trip_time"])
        berlin_pankow_entry.append(res["transports"][i]["transport_info"]["full_name"])
        berlin_pankow_entry.append(res["transports"][i]["stop_title"])
        timetable.append(berlin_pankow_entry)

