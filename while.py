# name = ''
# while name != 'Your name':
#     print('please type your name')
#     name = input()
# print('Thank You')

while True:
    print('Who are you ? ')
    name = input()
    if name == 'joe':
        print("Hello, joe. What is the password? (It is a fish.)")
        password = input()
        if password == "swordfish":
            print("Access granted.")
            break
    else:
        print("I'm fine, thanks. Who are you?")

print("Welcome " + name)
