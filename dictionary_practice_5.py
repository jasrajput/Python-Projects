allGuests = {
    "Jas": {'apples': 5, 'pepperoni': 4},
    "kamal": {'apples': 10, 'pepperoni': 2, 'pizza': 3}
}


def all_brought(guests, item):
    total = 0
    for k, v in guests.items():
        total = total + v.get(item, 0)
    return total


print("Number of things being brought")
print("- Total apples: " + str(all_brought(allGuests, 'apples')))
print("- Total pepperoni: " + str(all_brought(allGuests, 'pepperoni')))
