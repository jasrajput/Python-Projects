cities = {
    'patiala': {
        'country': 'INDIA',
        'population': '23,00000',
        'fact': 'Patiala is famous for many things'
    },
    'Los-angles': {
        'country': 'USA',
        'population': '3,500000',
        'fact': 'Los Angles is famous for Gambling'
    },
    'Assam': {
        'country': 'INDIA',
        'population': '3,500000',
        'fact': 'Assam is famous for Tea'
    }
}

for keys, values in cities.items():
    print("City name: " + keys)
    print("Country name: " + values['country'])
    print("Population: " + values['population'])
    print("Fact: " + values['fact'])
    print("\t")

dog = {
    'kind': 'cute',
    'owner': 'jas'
}

cat = {
    "kind": 'cute',
    'owner': 'kamal'
}

pets = [dog, cat]
for pet in pets:
    print(pet)

names = {
    'namew': 'jas',
    'class': 'msc'
}

# print(names['names'])
print(names.get('name', 'names'))
print(names.setdefault('name', 'jassa'))
print(names['name'])
