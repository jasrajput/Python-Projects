# check how many times a character appear
import pprint

message = "hey all, hows going on"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
