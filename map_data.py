# map_data.py

game_map = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'T', 'T', '.', '~', '~'],
    ['.', 'T', 'H', '.', '~', '~'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'T', 'T', '.'],
    ['.', '.', '.', '.', '.', '.']
]

def draw_map(game_map, player_pos):
    print("\n🌍 World Map:")
    for r in range(len(game_map)):
        for c in range(len(game_map[0])):
            if [r, c] == player_pos:
                print('P', end=' ')
            else:
                print(game_map[r][c], end=' ')
        print()
