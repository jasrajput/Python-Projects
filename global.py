def spam():
    global eggs
    eggs = 'spam'


def bacon():
    print(eggs)


eggs = 'global'
spam()
print(eggs)
print(bacon())
