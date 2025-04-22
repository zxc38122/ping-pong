from pygame import *
from random import *
from time import time as timer
mixer.init()
font.init()



window = display.set_mode((800,500))
clock = time.Clock()
display.set_caption('Пинг - понг')
Game_over = False
global bally
global ballx
bally = 1
ballx = 2

platformy = 4
fps = 40
qwerty123 = transform.scale(image.load('qweqwe.jpg'),(800,500))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,hei,wei):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(hei,wei))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 450 and self.rect.y > 50 :
            self.rect.y -= platformy
        if keys_pressed[K_s] and self.rect.y < 450 and self.rect.y > 50:
            self.rect.y += platformy
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 450 and self.rect.y > 50 :
            self.rect.y -= platformy
        if keys_pressed[K_DOWN] and self.rect.y < 450 and self.rect.y > 50:
            self.rect.y += platformy

    
class Ball(GameSprite):
    def update(self):
        global bally
        global ballx
        self.rect.y += bally
        self.rect.x += ballx
        if self.rect.y > 500:
            bally *= -1
            ballx *= -1
        if self.rect.y < 5:
            bally *= -1
            ballx *= -1
        if self.rect.x < 10:
            Game_over = False
        if self.rect.x > 790:
            Game_over = False
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


player1 = Player('roketka.png',10,200,0,50,10)
player2 = Player('roketka.png',780,200,0,50,10)
ball = Ball('ball123.png',390,240,0,10,10)


while Game_over != True:
    window.blit(qwerty123,(0,0))
    player1.update_l()
    player2.update_r()
    ball.update()
    ball.draw()
    player1.reset()
    player2.reset()
    if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
        ballx *= -1
        bally *= -1


display.update()
clock.tick(fps)
