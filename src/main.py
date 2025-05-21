import pygame
import player
import enemy
pygame.init()
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))

running = True
while running:
    liste = enemy.rechner_enemy_goto(enemy.enemy_rect,player.player_rect)
    enemy.enemy_move(liste)
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.movement()
    screen.blit(player.player,player.player_rect)
    screen.blit(enemy.enemy,enemy.enemy_rect)
    pygame.display.update()
pygame.quit()