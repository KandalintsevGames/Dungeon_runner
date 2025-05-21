"https://prod.liveshare.vsengsaas.visualstudio.com/join?3E802927391D7D3F91B11F6A7869B2A9F276"
import pygame
import player
pygame.init()
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))

running = True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.movement()
    screen.blit(player.player,player.player_rect)
    pygame.display.update()
pygame.quit()