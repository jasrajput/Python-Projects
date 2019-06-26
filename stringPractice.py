print('hello jas\'s')
print('hello jas\"s')
print('hello jas\\')
print('Hello there!\nHow are you?\n I\'m doing fine')
print(r'hello world') # raw string
letter = """Dear Alice, 

Everything's going bad.Come home

Sincerely, 
Jas
"""

greet = 'Could I be funny anymore ?'
num = '123434343'
print(greet[:5])
print(greet[6:])
if 'funny' in greet:
    print('You are really funny')
print(num.isalnum())
print(greet.isalnum())
# name = input("Enter a name")
# if name.isspace():
#     print('No spaces')
# else:
#     print('way to go')

warning = 'Please stay away from dogs'
print(','.join(warning))  # join() is called on a string value and is passed a list value.
print('ABC '.join(['my', 'name', 'is', 'jas']))
print(warning.split())  # split() method does the opposite: It’s called on a string value and returns a list of strings
print(warning.split('e'))  # It removes the specific character you want to remove.In this case  'e'
print(letter.split('\n'))
print(warning.rjust(31, '.'))
print(warning.ljust(31, '.'))
print(warning.center(51, '.'))
print(warning.strip('p'))