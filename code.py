from pygame import *
from random import *
from time import time as timer
mixer.init()
font.init()



window = display.set_mode((800,500))
clock = time.Clock()
display.set_caption('Пинг - понг')
global Game
Game = True
global bally
global ballx
bally = 2
ballx = 4
font = font.SysFont('Arial',50)
run = True
platformy = 8
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
        if keys_pressed[K_w] and  self.rect.y > 0 :
            self.rect.y -= platformy
        if keys_pressed[K_s] and self.rect.y < 451 :
            self.rect.y += platformy
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0 :
            self.rect.y -= platformy
        if keys_pressed[K_DOWN] and self.rect.y < 450 :
            self.rect.y += platformy

    
class Ball(GameSprite):
    def update(self):
        global bally
        global ballx
        self.rect.y += bally
        self.rect.x += ballx
        if self.rect.y > 490:
            bally *= -1
            ballx *= 1
        if self.rect.y < 5:
            bally *= -1
            ballx *= 1
        if self.rect.x < 20:
            Game = False
            win = 1
        if self.rect.x > 780:
            Game = False
            win = 2
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


player1 = Player('roketka.png',10,200,0,10,50)
player2 = Player('roketka.png',780,200,0,10,50)
ball = Ball('ball123.png',390,240,0,10,10)
win1 = font.render('Победил игрок слева!',True,[0,255,0])
win2 = font.render('Победил игрок справа!',True,[0,255,0])
while run:
    for e in event.get():
        if e.type == QUIT:
            Game = False

    while Game:
        for e in event.get():
            if e.type == QUIT:
                Game = False
    
        window.blit(qwerty123,(0,0))
        player1.update_r()
        player2.update_l()
        ball.update()
        ball.draw()
        player1.reset()
        player2.reset()
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            ballx *= -1
            randnum = randint(0,1)
            if randnum == 0:
                randy = 1
            elif randnum == 1:
                randy = -1
            bally *= randy
        display.update()
        clock.tick(fps)
    if win == 1:
        window.blit(win1,(300,200))
    elif win == 2:
        window.blit(win2,(300,200))



    display.update()
    clock.tick(fps)
