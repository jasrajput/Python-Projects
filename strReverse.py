# string[where to start slice:where to end slice:How many step], if empty, it goes the same way
def str_reverse(string):
    return string[::2]


print(str_reverse('python'))
