from pygame import *
from random import *

win = display.set_mode((720,480))

clock = time.Clock()

init()
img_genemi = font.Font(None, 50)

class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,30,100)
        self.speed = speed
        self.score = 0
        
        self.score_img = img_genemi.render(str(self.score), True,(222,33,5), (22,77,9))
        
    def move(self):
        key_list = key.get_pressed()
        if key_list[K_w]:
            self.hitbox.y -= self.speed
        if key_list[K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 480:
            self.hitbox.bottom = 480
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = ball.speed
            ball.random_x = randint(1,3)
            ball.random_y = randint(1,3)

    def autopilot(self):
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed
                
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed


class Ball():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,34,34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.random_x = 1
        self.random_y = 1
    def move(self):
        self.hitbox.x += self.speed_x * self.random_x
        self.hitbox.y += self.speed_y * self.random_y
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 480:
            self.speed_y = -self.speed
        if self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (360, 240)
            player1.score += 1
            player1.score_img = img_genemi.render(str(player1.score), True,(222,33,5), (22,77,9))
            time.wait(1000)
            self.random_x = 1
            self.random_y = 1
        if self.hitbox.right > 720:
            self.speed_x = -self.speed
            self.hitbox.center = (360, 240)
            
            player2.score += 1
            player2.score_img = img_genemi.render(str(player2s.score), True,(22,222,5), (44,22,91))
            time.wait(1000)


player1 = Player(50,240,5)
player2 = Player(620,240,1)
ball = Ball(360,240,2)

while True:
    win.fill((255,255,255))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win,(255,0,0),player1.hitbox)
    player2.autopilot()
    draw.rect(win,(255,0,0),player2.hitbox)
    ball.move()
    draw.rect(win,(255,0,0),ball.hitbox)
    win.blit(player1.score_img,(20,70))
    win.blit(player2.score_img,(680,70))
    display.update()
    clock.tick(200)

