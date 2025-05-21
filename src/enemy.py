import pygame

pygame.init()

enemy_size = (100,100)

enemy = pygame.image.load("enemy.png")
enemy1 = pygame.transform.scale(enemy,enemy_size)
enemy_rect = enemy.get_rect(center = (500,500))


def enemy_goto(player_rect,enemy_rect):
    x_cor_difference = enemy_rect.x - player_rect.x
    y_cor_difference = enemy_rect.y - player_rect.y
    length  = (y_cor_difference**2+x_cor_difference**2)**0.5
    if length <= 100:
        Enemy_Direction_x = 0
        Enemy_Direction_y  = 0
    else: 
        Enemy_Direction_x = x_cor_difference / length
        Enemy_Direction_y = y_cor_difference / length
    return [Enemy_Direction_x,Enemy_Direction_y]