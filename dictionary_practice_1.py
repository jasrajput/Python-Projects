characteristics = {
    'name': 'sophie',
    'disposition': 'loud',
    'size': 'fat',
    'color': 'grey'
}
print(characteristics['name'])
for key, val in characteristics.items():
    print(key, val)

birthdays = {
    'jas': 'june 11',
    'kamal': 'march 29'
}

while True:
    print("Enter name: ")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ", is the bday of " + name)
    else:
        print("I do not have such record")
        print("What is their birthday")
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

for name, val in birthdays.items():
    print(name, val)

