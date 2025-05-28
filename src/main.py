import pygame
import player
from enemy import init_enemy,enemy_goto
pygame.init()
background = pygame.image.load("src/assets/background.png")
x = 1920
y= 1080
screen = pygame.display.set_mode((x,y))
background_img = pygame.transform.scale(background,(x,y))

def game_loop():
    FPS = 144
    clock = pygame.time.Clock()
    running = True

    # init enemy
    enemy_size = (100,100)
    enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red,enemy_life_black = init_enemy(enemy_size)

    player_img , player_rect, batterie_color,batterie_base = player.player_init()
    player_life = 100
    test = 0

    #for optimization
    amount_cat = 4

    while running:
        fps = clock.get_fps()
        test +=1
        if test == amount_cat:
            screen.blit(background_img,(0,0))
        #screen.fill("white")
            test = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        enemy_rect_dictionary= player.Blitzi(enemy_rect_dictionary,amount_enemy)
        player.movement(player_rect)

        screen.blit(player_img,player_rect)
        batterie_color = pygame.transform.scale(batterie_color,(-450*(player_life/100),80))
        screen.blit(batterie_base,(x/2-50,900))
        screen.blit(batterie_color,(x/2-50+30,910))

        #enemy.enemy_rect = enemy.enemy.get_rect(center = (liste_enemy_movement[0],liste_enemy_movement[1]))
        for i in range(amount_enemy):
            if enemy_rect_dictionary[i][1] > 0:
                enemy_movement = enemy_goto(player_rect,enemy_rect_dictionary[i][0])
                enemy_rect_dictionary[i][0].x += enemy_movement[0]
                enemy_rect_dictionary[i][0].y += enemy_movement[1]
                enemy_life_red = pygame.transform.scale(enemy_life_red,(100*(enemy_rect_dictionary[i][1]/100),50))
                player_life = player.damage(player_life,enemy_movement[2]) 
                screen.blit(enemy_img,enemy_rect_dictionary[i][0])
                screen.blit(enemy_life_black,(enemy_rect_dictionary[i][0].x,enemy_rect_dictionary[i][0].y -30))
                screen.blit(enemy_life_red,(int(enemy_rect_dictionary[i][0].x),int(enemy_rect_dictionary[i][0].y-30)))
        pygame.display.update()
        print(fps)
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    game_loop()