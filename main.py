import pygame
import sys

from level import walls, start_x, start_y
from player import Player       
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, WALL_COLOR, PLAYER_COLOR, TILE_SIZE

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

player = Player(start_x, start_y) #Start Position wird aus Level geholt


running = True
while running:
    moved = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        #Bewegungen auf Tastatur abfragen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moved = player.move(-TILE_SIZE, 0, walls)   #player.move erwartet immer 3 Angaben (TILE_SIZE X-Achse, TILE_SIZE Y-Achse, liste walls))
            elif event.key == pygame.K_RIGHT:
                moved = player.move(TILE_SIZE, 0, walls)
            elif event.key == pygame.K_UP:
                moved = player.move(0, -TILE_SIZE, walls)
            elif event.key == pygame.K_DOWN:
                moved = player.move(0, TILE_SIZE, walls)

            if not moved:                              #Wenn player.moved nicht geht(False zurückgegeben wird), dann Fehlermeldung -> "Crash"
                print("Crash")        

    # Spieler darstellen
    screen.fill(BACKGROUND_COLOR)
    player.draw(screen, PLAYER_COLOR)               #Klasse Player übernimmt nun Jeder durchgang wird der Player "gezeichnet"
   
    # Wände darstellen
    for wall in walls:                              #Jeder durchgang werden die Wände gezeichnet
        pygame.draw.rect(screen, WALL_COLOR, wall)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()