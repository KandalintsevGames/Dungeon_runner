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
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                player_rect.y -= 5
            elif event.key == pygame.K_s:
                player_rect.y += 5
            elif event.key == pygame.K_a:
                player_rect.x -= 5
            elif event.key == pygame.K_d:
                player_rect.x += 5
    screen.blit(player,player_rect)
    pygame.display.update()
pygame.quit()