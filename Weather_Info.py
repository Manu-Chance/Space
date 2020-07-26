#! python3

import requests
import bs4
import datetime

current_time = datetime.datetime.now().time()
current_hour = str(datetime.datetime.now().time())[:-13]
print(f"The current time is {current_time}")
#current_hour = '05'

#user_location = "Bad Vilbel"
#user_location_parsed = "bad+vilbel"
user_location = input("Please enter your city:> ")
user_location_parsed = user_location.replace(" ", "+")

print(f"The weather in {user_location}:")

current_page = requests.get(f"https://www.metcheck.com/HOBBIES/astronomy_forecast.asp?zipcode={user_location_parsed}")
pageSoup = bs4.BeautifulSoup(current_page.text, "html.parser")
relevant_info = pageSoup.findAll("td", {"class": "dataTableDataRow"})

current_hour_display = int(current_hour) + 1

if len(relevant_info[39].getText()) > 5:
	init_pos = 42
else:
	init_pos = 39


if current_hour == '23':
	print()
	n = 0
	info_today = 5
elif current_hour == '00':
	print()
	n = 0
	info_today = 4
elif current_hour == '01':
	print()
	n = 0
	info_today = 3
elif current_hour == '02':
	print()
	n = 0
	info_today = 2
elif current_hour == '03':
	print()
	n = 0
	info_today = 1
else:
	n = 23 - int(current_hour) - 1
	info_today = 6
	current_hour_display = (23 - int(current_hour))
	current_hour_display = int(current_hour) + current_hour_display

skip_value = 12
init_pos = init_pos + (n * skip_value)

#print(current_hour)
#print(f"current_hour_dislpay:> {current_hour_display}")
# make current_hour_display loop over at 24:00
# idk yet how lul

for i in range(info_today):
	print(f"Pos {int(current_hour_display)%24 + i}:00:> {relevant_info[init_pos + (i * skip_value)].getText()}")
	print()























'''
for i in range(300):
	print(f"Pos:> {i} || {relevant_info[i].getText()}")
'''
