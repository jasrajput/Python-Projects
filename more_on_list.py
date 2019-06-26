spam = [1, 2, 3, 4]


def new_list(val):
    val[:-1] += ['and']
    return val


print(new_list(spam))
