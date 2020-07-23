#! python3

'''
# things to do:
# - create try exception statement to prevent crashing
# - create all the required statements (time, clearness, temperatur)
# - expand it to include the next 2 days
# - make a Telegram bot instead of using emails
# - add time delay to send update hourly between 2300 and 0400
'''

import requests
import bs4
import time
import os
import smtplib
import ssl
import datetime
import TempConv as TC # designed to convert the temperature

port = 465

user = 'princeugandan029@gmail.com'
passw = 'mbgZ48092a'
receive = 'manuel.pawollek@gmail.com'

user_location = input("Please enter your city:> ")
user_location_parsed = user_location.replace(" ", "+")


while True:
	print(f"The current weather in {user_location} \n\n")

	current_page = requests.get(f'https://www.metcheck.com/HOBBIES/astronomy_forecast.asp?zipcode={user_location_parsed}')
	pageSoup = bs4.BeautifulSoup(current_page.text, "html.parser")

	relevant_info = pageSoup.findAll("td", {"class": "dataTableDataRow"})

	cloud_status_today = relevant_info[39].getText()
	cloud_status_today = cloud_status_today[:-2]

	cloud_status_today_alt = relevant_info[42].getText()
	cloud_status_today_alt = cloud_status_today_alt[:-2]

	print(f"The current clouds cover {cloud_status_today}%")
	print(f"The current clouds cover {cloud_status_today_alt}%")

	subject = 'Subject test'
	content = 'Test Message'
	message = 'Subject: {}\n\n{}'.format(subject, content)

	context = ssl.create_default_context()
	print("[SENDING MESSAGE...] Starting to send.")
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
		server.login(user, passw)
		server.sendmail(user, receive, message)
	print("[MESSAGE SENT] Message has been sent.")
	break


	time.sleep(5)
	#time.sleep(3600)
	os.system('cls' if os.name =='nts' else 'clear')
