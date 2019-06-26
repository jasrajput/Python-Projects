file_name = 'test.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write('\tI love pizza\n')

with open(file_name, 'a') as file:
    file.write('sandwiches too')
