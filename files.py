filename = 'pi.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string = pi_string + line

print(pi_string.strip())
print(len(pi_string))
