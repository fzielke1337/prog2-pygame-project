import pygame
import sys

from level import walls
from settings import WIDTH, HEIGHT

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

player = pygame.Rect(480, 60, 60, 60)


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
                player.x -= 60
                moved = True
            elif event.key == pygame.K_RIGHT:
                player.x += 60
                moved = True
            elif event.key == pygame.K_UP:
                player.y -= 60
                moved = True
            elif event.key == pygame.K_DOWN:
                player.y += 60
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
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), player)
   
    # Wände darstellen
    for wall in walls: 
        pygame.draw.rect(screen, (0, 255, 0), wall)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()