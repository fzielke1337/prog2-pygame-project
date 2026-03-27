import pygame

# Wände erstellt durch Ausprobieren
wall_top = pygame.Rect(0, 0, 800, 10)
wall_bottom = pygame.Rect(0, 590, 800, 10)
wall_left = pygame.Rect(0, 0, 10, 600)
wall_right = pygame.Rect(790, 0, 10, 600)

# Alle Wände in Liste
walls = [wall_top, wall_bottom, wall_left, wall_right]