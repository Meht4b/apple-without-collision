import pygame
from classes import *
import random

pygame.init()

window = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

a = []
for i in range(50):
    a.append(rectangle(random.randint(1,1000),random.randint(1,1000),x:=random.randint(50,100),(x*255/100*0,x*255/100*0.7,x*255/100),x*10/100,x*10/100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    
    rectangle.classUpdate()
    redraw(window)

    clock.tick(60)




    