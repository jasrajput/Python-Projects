import json


def stored_username():
    file_name = 'username.json'
    try:
        with open(file_name) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = stored_username()
    if username:
        ask = input("is this correct username ")
        if ask == 'yes' or ask == 'yea' or ask == 'yeah':
            print("Welcome back, " + username + '!')
        else:
            get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


def get_new_username():
    file_name = 'username.json'
    username = input("What is your username ? ")
    with open(file_name, 'w') as file:
        json.dump(username, file)
    return username


greet_user()
