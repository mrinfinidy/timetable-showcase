import datetime
from time import sleep
import os

from stops.berlin_hbf import times_berlin_hbf
from stops.berlin_pankow import times_berlin_pankow
from stops.invalidenpark import times_invalidenpark


def get_date():
    today = datetime.date.today()
    day = datetime.datetime.strptime(str(today.day), "%d").strftime("%d") 
    month = datetime.datetime.strptime(str(today.month), "%m").strftime("%m")
    year = datetime.datetime.strptime(str(today.year), "%Y").strftime("%Y")
    return day + '.' + month + '.' + year


def get_time(station):
	# Add buffer to walk to station
	now = datetime.datetime.now()	
	if station == 'berlin_hbf':
		now + datetime.timedelta(minutes=2)
	elif station == 'berlin_pankow':
		now + datetime.timedelta(minutes=3)
	elif station == 'invalidenpark':
		now + datetime.timedelta(minutes=6)
	hour = datetime.datetime.strptime(str(now.hour), "%H").strftime("%H")
	minute = datetime.datetime.strptime(str(now.minute), "%M").strftime("%M")
	return hour + '%3A' + minute

def get_timetable(timetable):
	times_berlin_hbf(get_time('berlin_hbf'), get_date(), timetable)
	times_berlin_pankow(get_time('berlin_pankow'), get_date(), timetable)
	times_invalidenpark(get_time('invalidenpark'), get_date(), timetable)
	for row in timetable:
		if row == 0:
			print('\nBERLIN HAUPTBAHNHOF')
			continue
		if row == 1:
			print('\nBERLIN-PANKOW')
			continue
		if row == 2:
			print('\nINVALIDENPARK')
			continue
		print("{: >20} {: >20} {: >50}".format(*row))

while True:
    timetable = []
    _ = os.system('clear')
    get_timetable(timetable)
    sleep(30)


tracemalloc.stop()
