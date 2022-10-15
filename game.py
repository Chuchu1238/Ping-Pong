from random import randint
import time
from pygame import *


window = display.set_mode((700,500))
display.set_caption('Ping Pong')
background = transform.scale(image.load("back.jpg"),(700,500))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        display.update()