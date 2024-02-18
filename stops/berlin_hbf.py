import requests
import json

def times_berlin_hbf(time, date, timetable):
    url = 'https://www.fahrplan.guru/api/haltestelle?city=berlin&date=' + date + '&dir=dep&name=berlin-hauptbahnhof&state=berlin&time=' + time
    res = requests.get(url)
    res = json.loads(res.text)
    
    timetable.append(0) # indicate berlin hbf station

    for i in range(5):
        berlin_hbf_entry = []
        berlin_hbf_entry.append(res["transports"][i]["nearest_trip_time"])
        if 'full_name' in res["transports"][i]["transport_info"]:
            berlin_hbf_entry.append(res["transports"][i]["transport_info"]["full_name"])
        else:
            berlin_hbf_entry.append(res["transports"][i]["transport_info"]["line"])
        berlin_hbf_entry.append(res["transports"][i]["stop_title"])
        timetable.append(berlin_hbf_entry)
