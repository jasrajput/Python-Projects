import json

file_name = 'username.json'

with open(file_name) as file:
    username = json.load(file)
    print("Welcome back, " + username + '!')