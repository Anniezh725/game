# systems.py

import random
from player import add_item, inventory, home_pos

turn = 0

def get_time_of_day():
    return "🌞 Day" if turn % 10 < 5 else "🌙 Night"

def move_player(direction, pos, game_map):
    row, col = pos

    if direction == 'w':
        row -= 1
    elif direction == 's':
        row += 1
    elif direction == 'a':
        col -= 1
    elif direction == 'd':
        col += 1

    if 0 <= row < len(game_map) and 0 <= col < len(game_map[0]):
        return [row, col]

    print("🚫 You can't move there.")
    return pos

def craft_menu():
    print("\n⛺ Campsite")
    print("1. Cook Fish (2 fish)")
    print("2. Build Campfire (3 wood)")
    print("3. Leave")

    choice = input("> ")

    if choice == "1":
        if inventory["fish"] >= 2:
            inventory["fish"] -= 2
            print("🍖 You cooked a hearty meal!")
        else:
            print("❌ Not enough fish.")
    elif choice == "2":
        if inventory["wood"] >= 3:
            inventory["wood"] -= 3
            print("🔥 Campfire built!")
        else:
            print("❌ Not enough wood.")
    else:
        print("Leaving campsite.")

def interact(tile):
    global turn
    turn += 1

    print(f"\nTime: {get_time_of_day()}")

    if tile == '~':
        if random.random() < 0.7:
            add_item("fish")
        else:
            print("🎣 The fish got away.")

    elif tile == 'T':
        add_item("wood")

    elif tile == 'H':
        craft_menu()

    else:
        print("🌿 Quiet land.")

def wildlife_encounter():
    if get_time_of_day() == "🌙 Night" and random.random() < 0.3:
        print("🐺 A wild animal attacks!")
        if random.random() < 0.5:
            print("🏆 You scared it away.")
        else:
            print("💀 You flee back to camp!")
            return home_pos.copy()
    return None
