#создай игру "Лабиринт"!
from pygame import *

window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
display.set_caption('Побег с еврейского логова')
background = transform.scale(image.load('background.jpg'),(window_width,window_height))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= window_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_3
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.y = wall_y
        self.rect.x = wall_x
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
        draw.rect(window,(self.color_1,self.color_2,self.color_3),(self.rect.x,self.rect.y,self.width,self.height))



#igrovaya scena

player = Player('hero.png', 5, window_height - 80, 4)
evrey = Enemy('cyborg.png', window_width - 80, 280 , 2)
treasure = GameSprite('vihod.png',window_width - 120, window_height -80 ,0)

w1 = Wall(2,233,160,100,20,450,10)
w2 = Wall(2,233,160,100,480,350,10)
w3 = Wall(2,233,160,100,20,10,380)
w4 = Wall(2,233,160,220,100,10,380)
w5 = Wall(2,233,160,340,20,10,380)
w6 = Wall(2,233,160,440,100,10,380)
w7 = Wall(2,233,160,450,100,100,10)

game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.Font(None,100)
win = font.render('ты сбежал!',True,(225,215,0))
lose = font.render('тебя поймали!',True,(180,0,0))




#zvuki fon
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

defeat = mixer.Sound('defeat.ogg')
money = mixer.Sound('money.ogg')


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        player.update()
        evrey.update()



        player.reset()
        evrey.reset()
        treasure.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(player,evrey) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7):
            finish = True
            window.blit(lose,(135,200))
            defeat.play()
        if sprite.collide_rect(player,treasure):
            finish = True
            window.blit(win,(135,200))
            money.play()







    display.update()
    clock.tick(FPS)








