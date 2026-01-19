from pygame import *
import random  # Импортируем модуль random

win = display.set_mode((720, 480))
display.set_caption("Pong")  # Добавляем заголовок окну
clock = time.Clock()

class Player(sprite.Sprite):  # Наследуемся от sprite.Sprite
    def __init__(self, x, y, speed):
        super().__init__()  # Инициализация sprite
        self.image = Surface([50, 150])  # Создаем поверхность для игрока
        self.image.fill((255, 255, 255))  # Заполняем белым цветом
        self.rect = self.image.get_rect()  # Получаем прямоугольник из поверхности
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.width = 50
        self.height = 150
        self.x = x
        self.y = y

    def update(self): # Используем update вместо move
        key_list = key.get_pressed()
        if key_list[K_w]:
            self.rect.y -= self.speed 
        if key_list[K_s]:
            self.rect.y += self.speed
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.top < 0:
            self.rect.top = 0

    def autopilot(self):
        if ball.hitbox.cenetry < self.hitbox.cenetry:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y = self.speed
        if self.hitbox.collide_rect(ball.hitbox):
            ball.speed_x = -ball.speed

class Ball(sprite.Sprite):  # Наследуемся от sprite.Sprite
    def __init__(self, x, y, speed):
        super().__init__()  # Инициализация sprite
        self.image = Surface([34, 34])  # Создаем поверхность для мяча
        self.image.fill((255, 255, 255))  # Заполняем белым цветом
        self.rect = self.image.get_rect()  # Получаем прямоугольник из поверхности
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.width = 34
        self.height = 34
        self.x = x
        self.y = y

    def update(self): # Используем update вместо move
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom > 480:
            self.speed_y *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.left < 0:
            self.speed_y = -self.speed
            self.hitbox.center = (360,240)
            time.wait(1000)

            
        if self.rect.right > 720:
            self.speed_x *= -1


# Создаем спрайты
player1 = Player(20, 240, 5)  # Изменил координаты, чтобы не упирался в стену
player2 = Player(650, 240, 5) # Изменил координаты, чтобы не упирался в стену
ball = Ball(360, 240, 5)

# Создаем группы спрайтов
all_sprites = sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)

# Основной цикл игры
game = True
finish = False
while game:
    win.fill((0, 0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        # Движение и обновление спрайтов
        player1.update()
        ball.update()

        # "Автопилот" для второго игрока (упрощенная версия)
        if player2.rect.centery < ball.rect.centery:
            player2.rect.y += player2.speed
        elif player2.rect.centery > ball.rect.centery:
            player2.rect.y -= player2.speed

        
        if sprite.collide_rect(player1, ball):
            ball.speed_x *= -1
            ball.rect.x = player1.rect.right  
        if sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
            ball.rect.x = player2.rect.left  

        
        if player2.rect.bottom > 480:
            player2.rect.bottom = 480
        if player2.rect.top < 0:
            player2.rect.top = 0

        
        all_sprites.draw(win)

    clock.tick(60)  
    display.update()


