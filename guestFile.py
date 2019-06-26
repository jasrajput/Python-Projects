file_name = 'guestBook.txt'
with open(file_name, 'w') as file:
    i = 0
    while i < 4:
        print("Enter a name: ")
        name = input()
        print("welcome:", name)
        file.write("Name: " + name + "\n")
        i = i + 1
