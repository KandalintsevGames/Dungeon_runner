import pygame
import player
from player import player_init
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
    enemy_img, enemy_rect = init_enemy(enemy_size)

    player_img, player_rect = player_init()

    while running:

        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.movement(player_rect)
        screen.blit(player_img,player_rect)
        enemy_movement = enemy_goto(player_rect,enemy_rect)

        enemy_rect.x += enemy_movement[0]
        enemy_rect.y += enemy_movement[1]


        #enemy.enemy_rect = enemy.enemy.get_rect(center = (liste_enemy_movement[0],liste_enemy_movement[1]))
        
        screen.blit(enemy_img,enemy_rect)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
if __name__ == "__main__":
    game_loop()