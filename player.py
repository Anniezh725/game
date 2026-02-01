# player.py

player_pos = [3, 2]
home_pos = [2, 2]

inventory = {
    "fish": 0,
    "wood": 0
}

def add_item(item, amount=1):
    inventory[item] += amount
    print(f"+{amount} {item} (Total: {inventory[item]})")

def show_inventory():
    print("\n🎒 Inventory:")
    for item, qty in inventory.items():
        print(f"  {item}: {qty}")
