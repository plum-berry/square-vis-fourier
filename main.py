import math
import sys
import pygame
from pygame import gfxdraw

arg1 = sys.argv[1]
if arg1.isdigit():
    print("n = ",arg1)
    arg1 = int(arg1)
else:
    print("Invalid argument: arguments needs to be a integer")
    sys.exit(2)
pygame.init()
screen = pygame.display.set_mode((1500, 720))
pygame.display.set_caption("Square Wave generator using Fourier Series")
clock = pygame.time.Clock()
running = True

theta = 0 
yes = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

        #pygame.draw.circle(screen,"white",(300,300),200,width = 3)

       #gfxdraw.vline(screen,700,100,620,(255,255,255,100))
    x = 0
    y = 0
    theta -= 0.01
    for i in range(0,arg1):
        n = i*2 + 1 

        prevx = x
        prevy = y

        radius = int(150 * (4/(n * math.pi)))

        x += int(radius * math.cos(n * theta))
        y += int(radius * math.sin(n * theta))


        gfxdraw.aacircle(screen,prevx + 300,prevy + 300,radius,(255,255,255))
        gfxdraw.line(screen,prevx + 300,prevy + 300,x + 300,y+300,(255,255,255))
        gfxdraw.filled_circle(screen,x +300,y+300,5,(255,255,255))

    yes.insert(0,y)
    for i in range(len(yes)):
        gfxdraw.pixel(screen,710+i,yes[i]+300,(255,255,255))
    
    gfxdraw.line(screen,x+300,y+300,710,y+300,(255,255,255))
    # remove the points of the sine way as they go offscreen
    if len(yes)>700:
        yes.pop()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
