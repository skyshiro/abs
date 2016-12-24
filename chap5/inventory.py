def displayInventory( inventory):
    print("Inventory:")
    item_total = 0

    # Iterates over items in dictionary
    # K, and v are key and values in dictionary
    for k, v in inventory.items():
        item_total += v
        print( str(v) + ' ' + str(k))
        
    print("Total number of items: " + str(item_total))

def addToInventory( inventory, addedItems):
    # Iterate over list of items to add
    for loot in addedItems:
        # Try incrementing value in dictionary
        try:
            inventory[loot] += 1
        # If item doesn't exist, add to dictionary
        except KeyError:
            inventory[loot] = 1
    return inventory
            

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Dictionary uses a key:value
# dict[key] = value to access a value. also creates a new key if DNE
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory( inv)
inv = addToInventory( inv, dragonLoot)
displayInventory( inv)
