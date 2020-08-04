#! python3

import requests
import bs4
import datetime

current_time = datetime.datetime.now().time()
current_hour = str(datetime.datetime.now().time())[:-13]
print(f"The current time is {current_time}")
#current_hour = '01'

#user_location = "Bad Vilbel"
#user_location_parsed = "bad+vilbel"
user_location = input("Please enter your city:> ")
user_location_parsed = user_location.replace(" ", "+")
print()

print(f"The weather in {user_location} today:")

current_page = requests.get(f"https://www.metcheck.com/HOBBIES/astronomy_forecast.asp?zipcode={user_location_parsed}")
pageSoup = bs4.BeautifulSoup(current_page.text, "html.parser")
relevant_info = pageSoup.findAll("td", {"class": "dataTableDataRow"})

current_hour_display = int(current_hour) + 1

if len(relevant_info[39].getText()) > 5:
	init_pos = 42
else:
	init_pos = 39


if current_hour == '23':
	n = 0
	info_today = 5
	time_pos = 1
if current_hour == '00':
	n = 0
	info_today = 4
	time_pos = 2
elif current_hour == '01':
	n = 0
	info_today = 3
	time_pos = 3
elif current_hour == '02':
	n = 0
	info_today = 2
	time_pos = 4
elif current_hour == '03':
	n = 0
	info_today = 1
	time_pos = 5
else:
	n = 23 - int(current_hour) - 1
	info_today = 6
	current_hour_display = (23 - int(current_hour))
	current_hour_display = int(current_hour) + current_hour_display
	time_pos = 0

skip_value = 12
display_time = [23, 0, 1, 2, 3, 4]
init_pos = init_pos + (n * skip_value)


for i in range(info_today):
	if display_time[time_pos + i] == 23:
		print(f"Pos {display_time[time_pos + i]}:00:> {relevant_info[init_pos + (i * skip_value)].getText()}")
	else:
		print(f"Pos 0{display_time[time_pos + i]}:00:> {relevant_info[init_pos + (i * skip_value)].getText()}")
	print()


'''
for i in range(300):
	print(f"Pos:> {i} || {relevant_info[i].getText()}")
'''
