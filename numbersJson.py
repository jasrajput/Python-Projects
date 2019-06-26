import json

numbers = [1, 2, 3, 4, 5]
file_name = 'numbers.json'
with open(file_name, 'w') as file:
    json.dump(numbers, file)

with open(file_name) as file_obj:
    res = json.load(file_obj)

print(res)