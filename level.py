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

# Wände aus Level-Map generieren (Durchläuft die Level-Map und erstellt für jedes Wand Feld # ein pygame.Rect Objekt)
for zeile_index, zeile in enumerate(level_map):
    start_x = 0
    start_y = 0
    for spalte_index, feld in enumerate(zeile):
        if feld == "S":
            start_x = spalte_index * TILE_SIZE
            start_y = zeile_index * TILE_SIZE
        if feld == "#":
            x = spalte_index * TILE_SIZE
            y = zeile_index * TILE_SIZE
            wall = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            walls.append(wall)

