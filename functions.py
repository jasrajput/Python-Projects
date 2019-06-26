from printing_models import *


def make_album(artist_name, title, track=''):
    music_album = {'artist_name': artist_name, 'title': title}
    if track:
        music_album['track'] = track
    return music_album


# print(make_album('john doe', 'Hello world', track='12'))
# print(make_album('adoe', 'Hello world'))


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_mod = []

print_models(unprinted_designs[:], complete_mod)
show_completed_models(complete_mod)
print_models(unprinted_designs, complete_mod)


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


# make_pizza('margarita', 'tomato', 'zomato')


def build_profile(first_name, last_name, **user_info):
    profile = dict()
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, val in user_info.items():
        profile[key] = val
    return profile


# user_profile = build_profile(first_name='jas', last_name='rajput', hobby="programming", fav='pizza')
# print(user_profile)
