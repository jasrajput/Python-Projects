# find greater among numbers

#logic
# max = 20
# 20 > 20
# 32 > 20 = True , so we set max to 32
# max = 32 (now)


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

