secret_number = 9
guess = 0
guess_limit = 3
while guess < guess_limit:
    new = int(input("Guess "))
    guess = guess + 1
    if new == secret_number:
        print("you won")
        break
else:
    print("Sorry, you failed !")
