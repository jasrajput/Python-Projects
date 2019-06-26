active = True
while active:
    print("Enter you age: ")
    try:
        age = int(input())
        if age <= 3:
            print("Ticket is free")
            active = False
        elif (age > 3) and (age <= 12):
            print("Ticket costs $10")
            active = False
        elif age > 12:
            print("Ticket costs $15")
            active = False
    except ValueError:
        print("Age must be number")
