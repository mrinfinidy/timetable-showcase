import requests
import json

def times_invalidenpark(time, date, timetable):
    url = 'https://www.fahrplan.guru/api/haltestelle?city=berlin&date=' + date + '&dir=dep&name=invalidenpark&state=berlin&time=' + time
    res = requests.get(url)
    res = json.loads(res.text)

    timetable.append(2) # indicate invalidenpark station
    
    for i in range(3):
        invalidenpark_entry = []
        invalidenpark_entry.append(res["transports"][i]["nearest_trip_time"])
        invalidenpark_entry.append(res["transports"][i]["transport_info"]["full_name"])
        invalidenpark_entry.append(res["transports"][i]["stop_title"])
        timetable.append(invalidenpark_entry)        

