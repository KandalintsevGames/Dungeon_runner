# imports
import pygame
import player
from enemy import init_enemy,enemy_goto
import game_over


from killcount import text

pygame.init()

#screen setup
x = 1920
y= 1080
background = pygame.image.load("src/assets/background.png")
screen = pygame.display.set_mode((x,y), pygame.FULLSCREEN)
background_img = pygame.transform.scale(background,(x,y))

#gameloop
def game_loop():
    FPS = 144
    clock = pygame.time.Clock()
    running = True
    liste_der_Toden = []
    # init enemy
    enemy_size = (100,100)
    enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red,enemy_life_black = init_enemy(enemy_size)

    #init player
    player_img , player_rect, batterie_color,batterie_base = player.player_init()
    player_life = 100
    test = 0

    killcount_number = 0

    #for optimization
    amount_cat = 4
    
    while running:
        fps = clock.get_fps()
        print(fps)
        test +=1
        if test == amount_cat:
            screen.blit(background_img,(0,0))
        #screen.fill("white")
            test = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                enemy_rect_dictionary= player.Blitzi(enemy_rect_dictionary,amount_enemy)
        
        player.movement(player_rect,player_img)

        #Player drawing
        screen.blit(player_img,player_rect)

        #Battery drawing
        batterie_color = pygame.transform.scale(batterie_color,(450*(player_life/100),80))
        screen.blit(batterie_base,(x/2-50,900))
        screen.blit(batterie_color,(x/2-50+20,910))

        #enemy generating system
        repetition = 0
        damage_ges = 0
        for i in range(amount_enemy):
            # if there are enemies
            if enemy_rect_dictionary[i][1] > 0:
            # i = enemy_number
            # 1 = enemy_lifes

                enemy_movement = enemy_goto(player_rect,enemy_rect_dictionary[i][0])
                enemy_rect_dictionary[i][0].x += enemy_movement[0]
                enemy_rect_dictionary[i][0].y += enemy_movement[1]
                enemy_life_red = pygame.transform.scale(enemy_life_red,(100*(enemy_rect_dictionary[i][1]/100),50))
                damage_ges += enemy_movement[2]

                #drawing enemy 
                screen.blit(enemy_img,enemy_rect_dictionary[i][0])
                screen.blit(enemy_life_black,(enemy_rect_dictionary[i][0].x,enemy_rect_dictionary[i][0].y -30))
                screen.blit(enemy_life_red,(int(enemy_rect_dictionary[i][0].x),int(enemy_rect_dictionary[i][0].y-30)))

            
            else:
                repetition += 1
                
                if i not in liste_der_Toden:

                    killcount_number += 1
                    liste_der_Toden.append(i)

        if fps > 0 :
            player_life = player.damage(player_life,damage_ges/fps)

        if player_life < 50:
            batterie_color.fill((255,255,0))

        if player_life < 25:
            batterie_color.fill((255,0,0))
            
        if player_life >= 50:
            batterie_color.fill((0,255,0))
        if player_life <=0:
            overlay = pygame.Surface((1920,1080),pygame.SRCALPHA)
            overlay.fill((0,0,0,128))
            screen.blit(overlay,(0,0))
            running = game_over.game_over(screen)
            player_life = 100
        # if there are no enemies

        if repetition == amount_enemy:
            enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red,enemy_life_black = init_enemy(enemy_size)
            liste_der_Toden = []
            if player_life < 90:
                player_life += 10
        

        # to improve
        screen.blit(text(killcount_number),(50,50))

        #print(wave_live)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    game_loop()