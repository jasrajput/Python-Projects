file_name = 'programming.txt'
try:
    with open(file_name, 'w') as file:
        i = 0
        while i <= 3:
            print("why do you like programming ? ")
            file.write("why do you like programming ?\n")
            response = input()
            file.write("Response: " + response + '\n')
            i = i + 1

except FileNotFoundError:
    msg = "Sorry no such file name with: " + file_name
    print(msg)
