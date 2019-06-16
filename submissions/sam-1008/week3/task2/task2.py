import json
import csv
import requests

my_requests = requests.get('https://jsonplaceholder.typicode.com/posts')
menu_list = my_requests.json()

a = 0

file = open('task2.csv', 'w')
x = csv.writer(file)
x.writerow(['Column_names', 'UserId', 'Id', 'Body'])

for i in menu_list:
    for key in menu_list:
        x.writerow([key['title'], key['userId'], key['id'], key['body']])
