# imports
import bosse
import Start
import pygame
import player
from enemy import init_enemy,enemy_goto
import game_over
from killcount import text

from asset_source import start_location_path


pygame.init()




#gameloop function
def game_loop():
    extra = 0
    sound = 1
    wave = 0
    
    #screen setup
    x = 1920
    y=1080
    background = pygame.image.load(f"{start_location_path()}assets/background.png")
    screen = pygame.display.set_mode((x,y),pygame.FULLSCREEN)
    background_img = pygame.transform.scale(background,(x,y))
    
    font = pygame.font.Font(f"{start_location_path()}assets/10Pixel-Bold.ttf",int(50*(x/1920)))

    # basic pygame setup
    FPS = 144
    clock = pygame.time.Clock()
    running, options = Start.start(screen,x,y)
    liste_der_Toden = []
    amount_cat = 3
    while options:
        amount_cat,extra,sound = Start.option(screen,amount_cat,extra,sound,x,y)
        running, options = Start.start(screen,x,y)
    # init enemy
    enemy_size = (100,100)
    welle = 9
    enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red1,enemy_life_black = init_enemy(enemy_size,extra,x,y,welle )
    dictionary_bosse = bosse.bosse_init(enemy_rect_dictionary)
    
    #init player
    player_img_r , player_rect, batterie_color, batterie_base, player_img_l = player.player_init()
    player_life = 100
    test = 0


    count = 0                                   # to be improved 

    #killcount adjustment
    killcount_number = 0

    #for optimization
    
    
    # add sounds
    pygame.mixer.music.load(f"{start_location_path()}assets/Vladwave.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(sound)

    wave_end_sound = pygame.mixer.Sound(f"{start_location_path()}assets/achievement-video-game-type-1-230515.mp3")
    game_over_sound = pygame.mixer.Sound(f"{start_location_path()}assets/game-over-31-179699.mp3")
    enemy_hit_sound = pygame.mixer.Sound(f"{start_location_path()}assets/video-game-hit-noise-001-135821.mp3")
    wave_end_sound.set_volume(sound)
    game_over_sound.set_volume(sound)
    enemy_hit_sound.set_volume(sound)

    #mana
    mana = 20
    while running:#

        max_mana = 20
        if mana >= max_mana:
            manabar = pygame.image.load(f"{start_location_path()}assets/manabar1.png").convert_alpha()
        elif mana >= (max_mana/6)*5:
            manabar =pygame.image.load(f"{start_location_path()}assets/manabar2.png").convert_alpha()
        elif mana >= (max_mana/6)*4:
            manabar =pygame.image.load(f"{start_location_path()}assets/manabar3.png").convert_alpha()
        elif mana >= (max_mana/6)*3:
            manabar =pygame.image.load(f"{start_location_path()}assets/manabar4.png").convert_alpha()
        elif mana >= (max_mana/6)*2:
            manabar =pygame.image.load(f"{start_location_path()}assets/manabar5.png").convert_alpha()
        elif mana >= (max_mana/6)*1:
            manabar =pygame.image.load(f"{start_location_path()}assets/manabar6.png").convert_alpha()
        manabar = pygame.transform.scale(manabar,(80,80))
        
        text_Welle = font.render(f"Welle: {welle}",1, (255,255,255))
        welle_rect = text_Welle.get_rect(center= (1920/2,50))
        pygame.mixer.music.set_volume(sound)
        fps = clock.get_fps()
        # if fps > 0:                           # to be improved 
        #     if fps < 60 and count >= 7:       # to be improved
        #         count = 0                     # to be improved
        #         amount_cat += 1               # to be improved


        #count += 1                             # to be improved
        test +=1
        if test == amount_cat:
            screen.blit(background_img,(0,0))
            test = 0

        if mana < max_mana:
            mana += 2/fps
        

        # event loop setup
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mana
                if mana >= 2:
                    mana -= 2
                    print(mana)
                    pygame.mixer.Sound.play(enemy_hit_sound)
                    enemy_rect_dictionary= player.Blitzi(enemy_rect_dictionary,amount_enemy)

        
        if player.movement(player_rect,x,y) == 1:
            screen.blit(player_img_r,player_rect)
        if player.movement(player_rect,x,y) == 0:
            screen.blit(player_img_l,player_rect)
        #Welle drawing
        screen.blit(text_Welle,welle_rect)

        #Battery drawing
        batterie_color = pygame.transform.scale(batterie_color,(450*(player_life/100),80))
        screen.blit(batterie_base,(10,y-180))
        screen.blit(batterie_color,(10+20,y-170))
        print(mana)
        #enemy generating system
        repetition = 0
        damage_ges = 0
        for i in range(amount_enemy):
            if enemy_rect_dictionary[i][1] > 0:
                enemy_movement = enemy_goto(player_rect,enemy_rect_dictionary[i][0],enemy_rect_dictionary[i][2],enemy_rect_dictionary[i][4])
                enemy_rect_dictionary[i][0].x += enemy_movement[0]
                enemy_rect_dictionary[i][0].y += enemy_movement[1]
                enemy_life_red = pygame.transform.scale(enemy_life_red1,(enemy_rect_dictionary[i][6]*(enemy_rect_dictionary[i][1]/enemy_rect_dictionary[i][5]),50))
                enemy_life_black = pygame.transform.scale(enemy_life_black,(enemy_rect_dictionary[i][6],50))
                damage_ges += enemy_movement[2]
                screen.blit(enemy_rect_dictionary[i][3],enemy_rect_dictionary[i][0])
                screen.blit(enemy_life_black,(enemy_rect_dictionary[i][0].x,enemy_rect_dictionary[i][0].y -30))
                screen.blit(enemy_life_red,(int(enemy_rect_dictionary[i][0].x),int(enemy_rect_dictionary[i][0].y-30)))

            
            else:
                repetition += 1
                
                if i not in liste_der_Toden:

                    killcount_number += 1
                    liste_der_Toden.append(i)

        if fps > 0 :
            player_life = player.damage(player_life,damage_ges/fps)

        # Adjusting color of player healthbar
        if player_life < 50:
            batterie_color.fill((255,255,0))

        if player_life < 25:
            batterie_color.fill((255,0,0))
            
        if player_life >= 50:
            batterie_color.fill((0,255,0))

        # Menu after player death
        if player_life <=0:
            pygame.mixer.Sound.play(game_over_sound)
            
            overlay = pygame.Surface((x,y),pygame.SRCALPHA)
            overlay.fill((0,0,0,128))
            screen.blit(overlay,(0,0))
            running = game_over.game_over(screen)
            player_rect.centerx = x/2
            player_rect.centery = y/2
            player_life = 100
            enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red1,enemy_life_black = init_enemy(enemy_size,extra,x,y,welle)
            killcount_number = 0
            mana = max_mana
            welle = 9

        # if there are no enemies
        if repetition == amount_enemy:
            wave += 1
            pygame.mixer.Sound.play(wave_end_sound)
            # adjusting enemy parameters
            enemy_img, enemy_rect_dictionary, amount_enemy,enemy_life_red1,enemy_life_black = init_enemy(enemy_size,extra,x,y,welle)
            welle += 1
            if welle%10 == 0:
                enemy_rect_dictionary,amount_enemy = bosse.bosse_load(enemy_rect_dictionary,dictionary_bosse,amount_enemy,10)
            #list of killed enemies
            liste_der_Toden = []
            # adding lives to player after every wave
            if player_life < 90:
                player_life += 10

        # drawin killcount
        screen.blit(text(killcount_number),(50,50))
        screen.blit(manabar,(x-200,y-180))
        # updating screen options
        pygame.display.update()
        clock.tick(FPS)
    # quiting option
    quit()
    pygame.quit()
if __name__ == "__main__":
    game_loop()