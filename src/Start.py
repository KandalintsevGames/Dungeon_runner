import pygame
from asset_source import start_location_path
from pygame.locals import *#


def start(screen,x,y):
    logo_scale = (x*1.01,y*1.01)

    pygame.init()
    game = pygame.image.load(f"{start_location_path()}assets/wallpaper text.png").convert_alpha()
    game = pygame.transform.scale(game,logo_scale)

    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',int(100*(x/1920)))
    start_button = font1.render('Start' , True ,(255,255,255) )
    text1_rect = start_button.get_rect(center = (x/4,850*(x/1920)))
    text3 = font1.render('Options' , True ,(255,255,255) )
    text3_rect = text3.get_rect(center = (x/2,850*(x/1920)))
    text2 = font1.render('quit' , True ,(255,255,255) )
    text2_rect = text2.get_rect(center = (x*3/4,850*(x/1920)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] <= text1_rect.x + 300*(x/1920) and mouse[0] >= text1_rect.x - 300*(x/1920):
                    if mouse[1] <= text1_rect.y + 100*(x/1920) and mouse[1] >= text1_rect.y - 100*(x/1920):
                        running = True
                        return running, False
                if mouse[0] <= text3_rect.x + 300*(x/1920) and mouse[0] >= text3_rect.x - 300*(x/1920):
                    if mouse[1] <= text3_rect.y + 100*(x/1920) and mouse[1] >= text3_rect.y - 100*(x/1920):
                        running = False
                        return running, True
                if mouse[0] <= text2_rect.x + 300*(x/1920) and mouse[0] >= text2_rect.x - 300*(x/1920):
                    if mouse[1] <= text2_rect.y + 100*(x/1920) and mouse[1] >= text2_rect.y - 100*(x/1920):
                        running = False
                        return running, False
                
        screen.blit(start_button,text1_rect)
        screen.blit(text2,text2_rect)
        screen.blit(text3,text3_rect)
        screen.blit(game,(0,-200))
        pygame.display.update()
def option(screen,amount_cat,extra,sound,x,y):
    pygame.init()

    font = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',int(300*(x/1920)))
    font1 = pygame.font.Font(f'{start_location_path()}assets/10Pixel-Bold.ttf',int(100*(x/1920)))
    options =font.render('Options' , True ,(255,255,255) )
    text1 = font1.render(str(amount_cat) , True ,(255,255,255) )
    text1_rect = text1.get_rect(center = (610,500))
    text2 = font1.render("amount_cat: " , True ,(255,255,255) )
    text2_rect = text2.get_rect(center = (300,500))
    text3 = font1.render("quit" , True ,(255,255,255) )
    text3_rect = text3.get_rect(center = (100,800))
    text4 = font1.render(str(extra) , True ,(255,255,255) )
    text4_rect = text4.get_rect(center = (1300,700))
    text5 = font1.render("gegnermenge von 1 bis 9 + " , True ,(255,255,255) )
    text5_rect = text5.get_rect(center = (600,700))
    text6 = font1.render(f"{str(sound *100)}%" , True ,(255,255,255) )
    text6_rect = text4.get_rect(center = (610,600))
    text7 = font1.render("Lautstärke: " , True ,(255,255,255) )
    text7_rect = text5.get_rect(center = (600,600))
    x = 0
    while True:
        screen.fill("black")
        x+= 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] <= text3_rect.x + 300 and mouse[0] >= text3_rect.x - 300:
                   if mouse[1] <= text3_rect.y + 50*(1920/x) and mouse[1] >= text3_rect.y - 50*(1920/x):
                       return amount_cat,int(extra),int(sound)/100
                elif mouse[0] <= text1_rect.x + 100 and mouse[0] >= text1_rect.x - 100 and  mouse[1] <= text1_rect.y + 50 and mouse[1] >= text1_rect.y - 50:
                    while mouse[0] <= text1_rect.x + 100 and mouse[0] >= text1_rect.x - 100 and  mouse[1] <= text1_rect.y + 50*(1920/x) and mouse[1] >= text1_rect.y - 50*(1920/x):
                        mouse = pygame.mouse.get_pos()
                        keys =pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        if keys[K_1]:
                            amount_cat = 1
                        if keys[K_2]:
                            amount_cat = 2
                        if keys[K_3]:
                            amount_cat = 3 
                        if keys[K_4]:
                            amount_cat =  4
                        if keys[K_5]:
                            amount_cat =  5
                        if keys[K_6]:
                            amount_cat =  6
                        if keys[K_7]:
                            amount_cat =  7
                        if keys[K_8]:
                            amount_cat =  8
                        if keys[K_9]:
                            amount_cat =  9
                        text1 = font1.render(str(amount_cat) , True ,(255,255,255) )
                        screen.fill("black")
                        screen.blit(options,(300,100))
                        screen.blit(text1,text1_rect)
                        screen.blit(text2,text2_rect)
                        screen.blit(text3,text3_rect)
                        screen.blit(text4,text4_rect)
                        screen.blit(text5,text5_rect)
                        screen.blit(text6,text6_rect)
                        screen.blit(text7,text7_rect)
                        pygame.display.update()
                elif mouse[0] <= text4_rect.x + 100 and mouse[0] >= text4_rect.x - 100 and  mouse[1] <= text4_rect.y + 50 and mouse[1] >= text4_rect.y - 50:
                    extra = "0"
                    while mouse[0] <= text4_rect.x + 100 and mouse[0] >= text4_rect.x - 100 and  mouse[1] <= text4_rect.y + 50 and mouse[1] >= text4_rect.y - 50:
                        
                        
                        mouse = pygame.mouse.get_pos()
                        keys =pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_0:
                                    extra += "0"
                                if event.key == pygame.K_1:
                                    extra += "1"
                                if event.key == pygame.K_2:
                                    extra += "2"
                                if event.key == pygame.K_3:
                                    extra += "3"
                                if event.key == pygame.K_4:
                                    extra += "4"
                                if event.key == pygame.K_5:
                                    extra += "5"
                                if event.key == pygame.K_6:
                                    extra += "6"
                                if event.key == pygame.K_7:
                                    extra += "7"
                                if event.key == pygame.K_8:
                                    extra += "8"
                                if event.key == pygame.K_9:
                                    extra += "9"
                

                        
                        print(extra)
                        text4 = font1.render(str(int(extra)) , True ,(255,255,255) )
                        screen.fill("black")
                        screen.blit(options,(300,100))
                        screen.blit(text1,text1_rect)
                        screen.blit(text2,text2_rect)
                        screen.blit(text3,text3_rect)
                        screen.blit(text4,text4_rect)
                        screen.blit(text5,text5_rect)
                        screen.blit(text6,text6_rect)
                        screen.blit(text7,text7_rect)
                        pygame.display.update()
                elif mouse[0] <= text6_rect.x + 100 and mouse[0] >= text6_rect.x - 100 and  mouse[1] <= text6_rect.y + 50 and mouse[1] >= text6_rect.y - 50:
                    sound = "0"
                    while mouse[0] <= text6_rect.x + 100 and mouse[0] >= text6_rect.x - 100 and  mouse[1] <= text6_rect.y + 50 and mouse[1] >= text6_rect.y - 50:
                        
                        
                        mouse = pygame.mouse.get_pos()
                        keys =pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                keys = event.key
                                if event.key == pygame.K_0:
                                    if int(sound +"0") <= 100:

                                        sound += "0"
                                if event.key == pygame.K_1:
                                    if int(sound +"1") <= 100:

                                        sound += "1"
                                if event.key == pygame.K_2:
                                    if int(sound +"2") <= 100:

                                        sound += "2"
                                if event.key == pygame.K_3:
                                    if int(sound +"3") <= 100:

                                        sound += "3"
                                if event.key == pygame.K_4:
                                    if int(sound +"4") <= 100:

                                        sound += "4"
                                if event.key == pygame.K_5:
                                    if int(sound +"5") <= 100:

                                        sound += "5"
                                if event.key == pygame.K_6:
                                    if int(sound +"6") <= 100:

                                        sound += "6"
                                if event.key == pygame.K_7:
                                    if int(sound +"7") <= 100:

                                        sound += "7"
                                if event.key == pygame.K_8:
                                    if int(sound +"8") <= 100:

                                        sound += "8"
                                if event.key == pygame.K_9:
                                    if int(sound +"9") <= 100:

                                        sound += "9"
                        text6 = font1.render(f"{str(int(sound))}%" , True ,(255,255,255) )
                        screen.fill("black")
                        screen.blit(options,(300,100))
                        screen.blit(text1,text1_rect)
                        screen.blit(text2,text2_rect)
                        screen.blit(text3,text3_rect)
                        screen.blit(text4,text4_rect)
                        screen.blit(text5,text5_rect)
                        screen.blit(text6,text6_rect)
                        screen.blit(text7,text7_rect)
                        pygame.display.update()
        screen.blit(options,(300,100))
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)
        screen.blit(text3,text3_rect)
        screen.blit(text4,text4_rect)
        screen.blit(text5,text5_rect)
        screen.blit(text6,text6_rect)
        screen.blit(text7,text7_rect)
        pygame.display.update()
    