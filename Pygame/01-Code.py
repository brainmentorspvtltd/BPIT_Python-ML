import pygame
pygame.init()

# set the resolution of screen
screen = pygame.display.set_mode((1000,500))
red = 255,0,0

ball = pygame.image.load('Football.png')

x = 100
y = 100

moveX = 1
moveY = 1

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(red)
    # surface, (color), (x,y), radius
    # pygame.draw.circle(screen, (0,0,0), (x,y), 50)

    screen.blit(ball, (x,y))

    x += moveX
    y += moveY

    if x > 1000 - 313/2:
        moveX = -1
    elif y > 500 - 313/2:
        moveY = -1
    elif x < 0:
        moveX = 1
    elif y < 0:
        moveY = 1

    pygame.display.update()

