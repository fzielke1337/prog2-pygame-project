import pygame
from settings import WIDTH, HEIGHT, TILE_SIZE
from box import Box
# Level Map erstellt mit Außenwänden
level_map = [
    "##########",
    "#.......S#",
    "#.########",
    "#........#",
    "####.###.#",
    "#...B....#",
    "#.##.#####",
    "#........#",
    "########.#",
    "#Z.......#",
    "##########"
]

walls = []
boxes = []
# Wände aus Level-Map generieren (Durchläuft die Level-Map und erstellt für jedes Wand Feld # ein pygame.Rect Objekt)
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0
for zeile_index, zeile in enumerate(level_map):
    for spalte_index, feld in enumerate(zeile):
# da sich spalte/zeile_index * TILE_SIZE immer wiederholt hab ich es mal angepasst
        x = spalte_index * TILE_SIZE
        y = zeile_index * TILE_SIZE        

        if feld == "S":
            start_x = x
            start_y = y

        elif feld == "Z":
            goal_x = x
            goal_y = y

        elif feld == "#":
            wall = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)  # ggf. Klasse für Wall machen?! Nur nötig wenn Wände eine Eigenschaft bekommen 
            walls.append(wall)                              # append für hinzufügen der Wall in die Liste

        elif feld == "B":
            box = Box(x, y)                                 # kein TILE_SIZE benötigt weil es in der Klasse Box steht
            boxes.append(box)                               # append für hinzufügen der box in die Liste

#        if feld == "S":
#            start_x = spalte_index * TILE_SIZE
#            start_y = zeile_index * TILE_SIZE
#        if feld == "Z":
#            goal_x = spalte_index * TILE_SIZE
#            goal_y = zeile_index * TILE_SIZE
#        if feld == "#":
#            x = spalte_index * TILE_SIZE
#            y = zeile_index * TILE_SIZE
#        if feld == "B":                     #Box eingefügt aber fehler drin gewesen, hab die Wand mit Blöcken gepflastert und mit Wand überschrieben
#            x = spalte_index * TILE_SIZE
#            y = zeile_index * TILE_SIZE

#            wall = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
#            walls.append(wall)

goal_rect = pygame.Rect(goal_x, goal_y, TILE_SIZE, TILE_SIZE)

