import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PROG2 Spielprojekt")

clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 60, 60)
# Wall erstellt mithilfe von ChatGPT (verstanden und angepasst)
wall = pygame.Rect(300, 200, 200, 40)


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

    if player.colliderect(wall):
        print("Crash!")
        player.x = old_x
        player.y = old_y

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), wall)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()