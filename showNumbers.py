def show_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            print(str(i) + ' EVEN')
        else:
            print(str(i) + ' ODD')


show_numbers(10)