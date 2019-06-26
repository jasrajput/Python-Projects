def prime_number(limit):
    for i in range(limit):
        if not i % 2 == 0:
            print("Prime number " + str(i))
        else:
            print("Composite number " + str(i))


prime_number(30)
