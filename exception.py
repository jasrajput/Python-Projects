try:
    age = int(input('Age '))
    print(age)
except ValueError:
    print("Error: Invalid Value")
finally:
    print('Welcome')
