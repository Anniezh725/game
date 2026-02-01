# main.py

from map_data import game_map, draw_map
from player import player_pos, show_inventory
from systems import move_player, interact, wildlife_encounter

def main():
    print("🎮 Welcome to the Wilderness Game!")

    while True:
        draw_map(game_map, player_pos)
        show_inventory()

        tile = game_map[player_pos[0]][player_pos[1]]
        interact(tile)

        new_pos = wildlife_encounter()
        if new_pos:
            player_pos[:] = new_pos

        move = input("\nMove (WASD | I=Inventory | Q=Quit): ").lower()

        if move == 'q':
            print("👋 Thanks for playing!")
            break
        elif move == 'i':
            show_inventory()
            continue
        elif move in ['w', 'a', 's', 'd']:
            player_pos[:] = move_player(move, player_pos, game_map)

if __name__ == "__main__":
    main()
