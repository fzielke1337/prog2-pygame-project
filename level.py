import pygame
from settings import WIDTH, HEIGHT, TILE_SIZE

# Level Map erstellt mit Außenwänden
level_map = [
    "##########",
    "#.......S#",
    "#.########",
    "#........#",
    "########.#",
    "#........#",
    "#.########",
    "#........#",
    "########.#",
    "#Z.......#",
    "##########"
]

walls = []
tile_size = TILE_SIZE


# Wände aus Level-Map generieren (Durchläuft die Level-Map und erstellt für jedes Wand Feld # ein pygame.Rect Objekt)
for zeile_index, zeile in enumerate(level_map):
    for spalte_index, feld in enumerate(zeile):
        if feld == "#":
            x = spalte_index * tile_size
            y = zeile_index * tile_size
            wall = pygame.Rect(x, y, tile_size, tile_size)
            walls.append(wall)

