import json

file_name = 'fav_number.json'


def stored_number():
    try:
        with open(file_name) as file:
            msg = json.load(file)

    except FileNotFoundError:
        get_number()

    else:
        print("I know your fav number is: " + str(msg))


def get_number():
    with open(file_name, 'w') as filing:
        fav_number = int(input("What's is your fav number ? "))
        json.dump(fav_number, filing)


stored_number()
