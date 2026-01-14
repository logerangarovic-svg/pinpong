from pygame import *
win = display.set_mode((720,480))
clock = time.Clock()

class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 50, 150)
        self.speed = speed
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
player1 = Player(200, 40,1)

class Ball():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 34, 34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed  
    def move(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.bottom > 480:
            self.speed_y *= -1
        if self.hitbox.top < 0:
            self.speed_y *= -1
        if self.hitbox.left < 0:
            self.speed_x *= -1
        if self.hitbox.right > 720:
            self.speed_x *= -1
ball1 = Ball(180,42,10)



while True:
    win.fill((0, 0, 0))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win, (255, 0, 0), player1.hitbox)
    ball1.move()
    
    if player1.hitbox.colliderect(ball1.hitbox):
        ball1.speed_x *= -1  
    draw.rect(win, (255, 200, 0), ball1.hitbox)


    clock.tick(120)
    display.update()
