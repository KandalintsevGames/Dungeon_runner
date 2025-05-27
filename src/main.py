import pygame
import player
from enemy import init_enemy,enemy_goto
pygame.init()
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))


def game_loop():
    FPS = 60
    clock = pygame.time.Clock()
    running = True

    # init enemy
    enemy_size = (100,100)
    enemy_img, enemy_rect_dictionary, amount_enemy = init_enemy(enemy_size)

    player_img , player_rect = player.player_init()

    while running:

        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.movement(player_rect)
        screen.blit(player_img,player_rect)
        

        

        #enemy.enemy_rect = enemy.enemy.get_rect(center = (liste_enemy_movement[0],liste_enemy_movement[1]))
        
        for i in range(amount_enemy):
            enemy_movement = enemy_goto(player_rect,enemy_rect_dictionary[i])
            enemy_rect_dictionary[i].x += enemy_movement[0]
            enemy_rect_dictionary[i].y += enemy_movement[1]
            #if enemy_movement[2] > 0:
            #    player_life = player.damage(enemy_movement[2],player_life) 
            screen.blit(enemy_img,enemy_rect_dictionary[i])
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
if __name__ == "__main__":
    game_loop()