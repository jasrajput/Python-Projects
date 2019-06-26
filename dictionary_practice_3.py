favourite_language = {
    'jen': ['Python', 'Ruby'],
    'sarah': ['C'],
    "phil's": ['Python', 'Haskell'],
    "Edward's": ['Ruby', 'Go']
}

for name, language in favourite_language.items():
    if len(language) == 1:
        print(name + " favorite language is: ")
        for fav_language in language:
            print("\t" + str(fav_language))
    else:
        print(name + " favourite language are: ")
        for fav_language in language:
            print("\t" + fav_language.title())

users = {
    "jas": {
        'first_name': 'jas',
        'last_name': 'rajput',
        'location': 'punjab'
    },
    "kamal": {
        'first_name': 'kamal',
        'last_name': 'deep',
        'location': 'punjab'
    }
}

for user, detail in users.items():
    print("username: " + user)
    full_name = detail['first_name'] + detail['last_name']
    print("\t Full name: " + full_name)
    print('\t location: ' + detail['location'])