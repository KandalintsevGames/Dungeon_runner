import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1920,1080))

player = pygame.image.load("player.gif")
player_rect = player.get_rect()
running = True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            player_rect.y += 5

    screen.blit(player,player_rect)
    pygame.display.update()
pygame.quit()