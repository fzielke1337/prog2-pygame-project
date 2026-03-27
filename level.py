import pygame
from settings import WIDTH, HEIGHT


# Wände erstellt durch Ausprobieren
wall_top = pygame.Rect(0, 0, WIDTH, 10)
wall_bottom = pygame.Rect(0, 590, WIDTH, 10)
wall_left = pygame.Rect(0, 0, 10, HEIGHT)
wall_right = pygame.Rect(790, 0, 10, HEIGHT)

# Alle Wände in Liste
walls = [wall_top, wall_bottom, wall_left, wall_right]