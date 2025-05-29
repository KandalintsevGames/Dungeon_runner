import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))

font = pygame.font.Font("src/assets/pixelart.ttf",50)

killcount = 0 

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                killcount += 1
    text = font.render(f"hello_World: {killcount}",1, (255,255,255))
    screen.blit(text,(50,50))
    pygame.display.update()
pygame.quit()