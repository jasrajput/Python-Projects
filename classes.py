class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, I am " + self.name)

    def listen(self):
        print('Listen up')


person1 = Person('Jas Rajput')
print(person1.name)
person1.talk()

person2 = Person("Bob smith")
print(person2.name)
person2.talk()
