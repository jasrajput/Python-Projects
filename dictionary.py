
Data = {
        'name': 'jas',
        'class': 'MSC(I.T)',
        'rollNo': 1713
}
print(Data['name'])

phone = input('Phone ')
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": 'three'
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, '!') + " "
print(output)

message = input("< ")
words = message.split(' ')
emoji_mapping = {
    ':(': "😚",
    "happy": '😂'
}

output = ''
for char in words:
    output += emoji_mapping.get(char, char) + " "
print(output)