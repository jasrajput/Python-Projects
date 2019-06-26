filename = 'test.txt'
with open(filename) as file_object:
    read = file_object.readlines()

for reading in read:
    index = reading.index('python')
    print(index)
