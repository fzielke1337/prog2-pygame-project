import pygame
import sys

from level import walls
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, WALL_COLOR, PLAYER_COLOR, TILE_SIZE

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

player = pygame.Rect(480, 60, TILE_SIZE, TILE_SIZE)


# Kollision auf False setzen
collision_active = False

running = True
while running:
    old_x = player.x
    old_y = player.y
    moved = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegung nur ein Feld pro Drücken // Mit der Hilfe von ChatGPT, verstanden und angepasst
    # vorher get_pressed() = dauerhafte Bewegung, jetzt KEYDOWN = einmal pro Taste drücken
        if event.type == pygame.KEYDOWN:
            old_x = player.x
            old_y = player.y
        

            if event.key == pygame.K_LEFT:
                player.x -= TILE_SIZE
                moved = True
            elif event.key == pygame.K_RIGHT:
                player.x += TILE_SIZE
                moved = True
            elif event.key == pygame.K_UP:
                player.y -= TILE_SIZE
                moved = True
            elif event.key == pygame.K_DOWN:
                player.y += TILE_SIZE
                moved = True

    # Nur 1 Mal Crash printen, kein Durchlaufen durch die Wand
    if moved == True:
        collision = False
        for wall in walls:
            if player.colliderect(wall):
                collision = True
                if not collision_active:
                    print("Crash")
                    collision_active = True
                player.x = old_x
                player.y = old_y
                break
   

    # Spieler darstellen
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
   
    # Wände darstellen
    for wall in walls: 
        pygame.draw.rect(screen, WALL_COLOR, wall)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()