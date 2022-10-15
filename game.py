from random import randint
import time
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,z):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,z))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 354:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 354:
            self.rect.y += self.speed


window = display.set_mode((700,500))
display.set_caption('Ping Pong')
background = transform.scale(image.load("back.jpg"),(700,500))
player1 = Player('1.png',10,175,5,24,136) 
player2 = Player('1.png',670,175,5,24,136)
ball = GameSprite('ball.png',320,240,7,60,60)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        
        window.blit(background, (0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update2()
        ball.reset()
        display.update()