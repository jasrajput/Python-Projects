def count_words(file_name):
    try:
        with open(file_name) as file:
            contents = file.read()
    except FileNotFoundError:
        msg = "sorry does'nt exist file named " + file_name
        print(msg)
    else:
        # read the contents of a file
        words = contents.split()  # will return a list
        length = len(words)
        print("File " + file_name + " has about (approx.) " + str(length) + ' characters')


file = ['programming.txt', 'guestBook.txt', 'test.txt', 'guest.txt', 'testing.txt']
for file_name in file:
    count_words(file_name)
