#hier entsteht die Klasse-Kisten

import pygame
from settings import TILE_SIZE

class Box:                                                      # Klasse für Box
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)     # wieder einfaches Rechteck mit TILE_SIZE x TILE_SIZE

    def draw(self, screen):                                     # erstellen der Box auf Bildschirm
        pygame.draw.rect(screen, (139, 69, 19), self.rect)      # aus pygame.org, feste Reihenfolge durch pygame (Wohin, Farbe, position + Rechteck (ggf. Rahmen)) 
        pygame.draw.rect(screen, (90, 45, 10), self.rect, 3)    # aus pygame.org, feste Reihenfolge durch pygame (Wohin, Farbe des Rahmens, Rechteck mit Rahmen))



