stuff = {
    'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12
}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    total = 0
    print("Inventory: ")
    for key in inventory:
        print(str(inventory[key]) + " " + str(key))
        total = total + inventory[key]
    print("Total number of items: " + str(total))
    return total


# display_inventory(stuff)


def add_to_inventory(inventory, loot_list):
    for i in range(len(loot_list)):
        if loot_list[i] in inventory:
            inventory[loot_list[i]] = inventory[loot_list[i]] + 1
        else:
            inventory.setdefault(loot_list[i], 1)
    return inventory


res = add_to_inventory(stuff, dragonLoot)
display_inventory(res)
