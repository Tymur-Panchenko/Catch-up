import pygame

setting_win = (600, 500)
bg_image = pygame.image.load("background.png.png")
hero1_image = pygame.image.load("hero1.png.png")
hero2_image = pygame.image.load("hero2.png.png")

pygame.init()

window = pygame.display.set_mode(setting_win)
pygame.display.set_caption("CATCH-UP")

clock = pygame.time.Clock()

game = True

x1,y1, x2,y2 = 150, 200, 400, 200
speed = 10

while game:
    window.blit(bg_image, (0,0))

    window.blit(hero1_image, (x1,y1))
    window.blit(hero2_image, (x2,y2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pressed = pygame.key.get_pressed()
    


    #HERO1
    if pressed[pygame.K_a] and x1 > 0:
        x1 -= speed


    if pressed[pygame.K_d] and x1 + 75 < setting_win[0]:
        x1 += speed

    if pressed[pygame.K_w] and y1 > 0:
        y1 -= speed

    if pressed[pygame.K_s] and y1 + 75 < setting_win[1]:
        y1 += speed


    #HERO2
    
    if pressed[pygame.K_LEFT] and x2 > 0:
        x2 -= speed


    if pressed[pygame.K_RIGHT] and x2 + 75 < setting_win[0]:
        x2 += speed

    if pressed[pygame.K_UP] and y2 > 0:
        y2 -= speed

    if pressed[pygame.K_DOWN] and y2 + 75 < setting_win[1]:
        y2 += speed
    
    clock.tick(60)
    pygame.display.flip()