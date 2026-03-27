import pygame
import sys

from level import walls
from player import Player       #hinzugefügt 27.03.26 20:05
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, WALL_COLOR, PLAYER_COLOR, TILE_SIZE

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

#player = pygame.Rect(480, 60, TILE_SIZE, TILE_SIZE)
player = Player(480, 60) #Start Position wird noch vorgegeben (Tile_Size ist in class Player hinterlegt)

# Kollision auf False setzen
# collision_active = False

running = True
while running:
#    old_x = player.x
#    old_y = player.y
    moved = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegung nur ein Feld pro Drücken // Mit der Hilfe von ChatGPT, verstanden und angepasst
    # vorher get_pressed() = dauerhafte Bewegung, jetzt KEYDOWN = einmal pro Taste drücken

 #           old_x = player.x               übernimmt player.py
 #           old_y = player.y               übernimmt player.py
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moved = player.move(-TILE_SIZE, 0, walls)
            elif event.key == pygame.K_RIGHT:
                moved = player.move(TILE_SIZE, 0, walls)
            elif event.key == pygame.K_UP:
                moved = player.move(0, -TILE_SIZE, walls)
            elif event.key == pygame.K_DOWN:
                moved = player.move(0, TILE_SIZE, walls)

            if moved is False:
                print("Crash")        

#            if event.key == pygame.K_LEFT:
#                player.x -= TILE_SIZE
#                moved = True
#            elif event.key == pygame.K_RIGHT:
#                player.x += TILE_SIZE
#                moved = True
#            elif event.key == pygame.K_UP:
#                player.y -= TILE_SIZE
#                moved = True
#            elif event.key == pygame.K_DOWN:
#                player.y += TILE_SIZE
#                moved = True

#    # Nur 1 Mal Crash printen, kein Durchlaufen durch die Wand
#    if moved == True:
#        collision = False
#        for wall in walls:
#            if player.colliderect(wall):
#                collision = True
#                if not collision_active:
#                    print("Crash")
#                    collision_active = True
#                player.x = old_x
#                player.y = old_y
#                break
   

    # Spieler darstellen
    screen.fill(BACKGROUND_COLOR)
    player.draw(screen, PLAYER_COLOR) #Klasse übernimmt nun
   
    # Wände darstellen
    for wall in walls: 
        pygame.draw.rect(screen, WALL_COLOR, wall)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()