import pygame
from settings import WIDTH, HEIGHT

level_map = [
    "##########"
    "#........#"
    "#........#"
    "#........#"
    "##########"
]

walls = []
tile_size = 80

for zeile_index, zeile in enumerate(level_map):
    for spalte_index, feld in enumerate(zeile):
        if feld == "#":
            x = spalte_index * tile_size
            y = zeile_index * tile_size
            wall = pygame.Rect(x, y, tile_size, tile_size)
            walls.append(wall)

