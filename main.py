import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 60, 60)

# Wände erstellt durch Ausprobieren
wall_top = pygame.Rect(0, 0, 800, 10)
wall_bottom = pygame.Rect(0, 590, 800, 10)
wall_left = pygame.Rect(0, 0, 10, 600)
wall_right = pygame.Rect(790, 0, 10, 600)

# Kollision auf False setzen
collision_active = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegungscode basierend auf Erklärung durch ChatGPT (verstanden und angepasst)
    keys = pygame.key.get_pressed()

    old_x = player.x
    old_y = player.y

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Nur 1 Mal Crash printen, kein Durchlaufen durch die Wand
    if (
        player.colliderect(wall_top) 
        or player.colliderect(wall_bottom) 
        or player.colliderect(wall_left) 
        or player.colliderect(wall_right)
        ):
        if not collision_active:
            print("Crash")
            collision_active = True
        player.x = old_x
        player.y = old_y
    else: 
        collision_active = False


    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), wall_top)
    pygame.draw.rect(screen, (0, 255, 0), wall_bottom)
    pygame.draw.rect(screen, (0, 255, 0), wall_left)
    pygame.draw.rect(screen, (0, 255, 0), wall_right)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()