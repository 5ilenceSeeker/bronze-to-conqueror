import json,os
import requests

my = requests.get('https://jsonplaceholder.typicode.com/comments')

menu = my.json()

#make some space for emails

Email = []

for i in menu:
	for j in menu:
            Email.append(j['email'])


uniqueEmails = sorted(set(Email))

for i in uniqueEmails:
	print (i)
