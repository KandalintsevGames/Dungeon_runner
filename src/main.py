import pygame

pygame.init()
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))

player = pygame.image.load("player.gif")
player_rect = player.get_rect()
player_rect.y = y/2
player_rect.x = x/2
running = True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    pygame.display.update()
pygame.quit()