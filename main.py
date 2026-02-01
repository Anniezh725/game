# main.py

import pygame
from map_data import game_map
from player import player_pos
from systems import move_player, interact, wildlife_encounter

# ===== PYGAME SETUP =====
pygame.init()

TILE_SIZE = 64
ROWS = len(game_map)
COLS = len(game_map[0])

WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌲 Wilderness Game")

clock = pygame.time.Clock()

# ===== COLORS =====
COLORS = {
    '.': (50, 200, 50),    # grass
    'T': (16, 120, 16),    # forest
    '~': (40, 100, 200),   # water
    'H': (180, 140, 90)    # camp
}

PLAYER_COLOR = (200, 50, 50)

# ===== DRAWING =====
def draw_world():
    for r in range(ROWS):
        for c in range(COLS):
            tile = game_map[r][c]
            color = COLORS.get(tile, (0, 0, 0))

            rect = pygame.Rect(
                c * TILE_SIZE,
                r * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    # draw player
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        pygame.Rect(
            player_pos[1] * TILE_SIZE,
            player_pos[0] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )
    )

# ===== MAIN LOOP =====
def main():
    running = True

    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        draw_world()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                old_pos = player_pos.copy()

                if event.key == pygame.K_w:
                    player_pos[:] = move_player('w', player_pos, game_map)
                elif event.key == pygame.K_s:
                    player_pos[:] = move_player('s', player_pos, game_map)
                elif event.key == pygame.K_a:
                    player_pos[:] = move_player('a', player_pos, game_map)
                elif event.key == pygame.K_d:
                    player_pos[:] = move_player('d', player_pos, game_map)

                # Only interact if movement happened
                if player_pos != old_pos:
                    tile = game_map[player_pos[0]][player_pos[1]]
                    interact(tile)

                    new_pos = wildlife_encounter()
                    if new_pos:
                        player_pos[:] = new_pos

    pygame.quit()

if __name__ == "__main__":
    main()
