def displayInventory( inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print( str(v) + ' ' + str(k))
        
    print("Total number of items: " + str(item_total))

def addToInventory( inventory, addedItems):
    currentInventory = list( inventory.keys())
    
    for loot in addedItems:
        try:
            inventory[loot] += 1
        except KeyError:
            inventory[loot] = 1
    return inventory
            

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory( inv, dragonLoot)
displayInventory( inv)
