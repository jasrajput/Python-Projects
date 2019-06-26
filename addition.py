i = 0
while True:
    try:
        first_num = int(input("Enter First number"))
        sec_num = int(input("Enter Second number"))
    except ValueError:
        print("Sorry only numbers")
    else:
        result = first_num + sec_num
        print("Addition of " + str(first_num) + " and " + str(sec_num) + ' is ' + str(result))
    # i = i + 1
