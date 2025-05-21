import pygame
import player
import enemy
pygame.init()
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))

def game_loop():
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    while running:

        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.movement()
        screen.blit(player.player,player.player_rect)
        liste_enemy_movement = enemy.enemy_goto(player.player_rect,enemy.enemy_rect)

        print(liste_enemy_movement)
        enemy.enemy_rect = enemy.enemy.get_rect(center = (enemy.enemy_rect.x + liste_enemy_movement[0],enemy.enemy_rect.y + liste_enemy_movement[1]))
        screen.blit(enemy.enemy1,enemy.enemy_rect)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()