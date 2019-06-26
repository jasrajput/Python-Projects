pets = ['cat', 'dog', 'lion', 'elephant']
print("What's your pet name")
pet_exist = input()
if pet_exist not in pets:
    print("sorry, no such pet name " + pet_exist)
else:
    print("The Pet with name " + pet_exist + " exist")

names = []
print("Enter name you want to add to our database")
while True:
    name = input()
    names = names + [name]
    if name == '':
        break
print("Names are: ")
for name in names:
    print(name)

