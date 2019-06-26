favourite_numbers = {
    'jas': '7',
    'kamal': '3',
    'gurpal': '6',
    'harman': '1',
    'safe': '9'
}

i = 1
while i < 10:
    print("Enter your name or (blank to quit)")
    name = input()
    if name == '':
        break
    if name in favourite_numbers:
        print(favourite_numbers[name] + " is the fav number of " + name)
    else:
        print("We do not have such record,let us know about their fav number")
        print("Enter your fav number")
        value = input()
        favourite_numbers[name] = value
        print("New Record added")
for names, values in favourite_numbers.items():
    # for val in values:
    print("fav number of " + names + " is: " + values + '\n')
