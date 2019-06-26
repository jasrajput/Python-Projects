def check(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Find upper: " + str(upper))
    print("Find Lower: " + str(lower))


check('HELLOWORLDs')