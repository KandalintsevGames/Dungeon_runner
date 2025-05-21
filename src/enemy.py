import pygame 
import math
enemy_pic = "src/assets/enemy.jpg"
enemy = pygame.image.load(enemy_pic)
enemy_rect= enemy.get_rect()

def rechner_enemy_goto(enemy_rect,player_rect):
    
    goto_y = player_rect.y - enemy_rect.y
    goto_x = player_rect.x - enemy_rect.x
    goto_y_2 = 5*(goto_y/(goto_x**2+goto_y**2))
    goto_x_2 = 5*(goto_x/(goto_x**2+goto_y**2))
def enemy_move(liste):
    enemy_rect.x += int(liste[0])
    enemy_rect.y += int(liste[1])
