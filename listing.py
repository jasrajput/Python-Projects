pet = [
    ['cats', 'dogs', 'shark', 'lion'],
    [10, 20, 30],
    ['home, kitchen, stuff, sofa, cushion']
]
print(pet[::-1])
del pet[0][1]
print((pet[0][1] + pet[0][2]) * 3)
print(pet[0][1] + pet[0][2])

names = []
while True:
    print("Enter the name of cat or nothing to stop.:")
    name = input()
    if name == '':
        break
    names += [name]
print("The cat names are: ")
for name in range(len(names)):
    print("index " + str(name) + " Name: " + names[name])
# index = str(name)
# value = names[name]

