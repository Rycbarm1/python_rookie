import pygame


from time import sleep
from threading import Thread
from pygame import image
from pygame.sprite import Sprite

class AlienBullets(Sprite):

    def __init__(self,ai_game,alien):

        """ 在外星人当前位置创建子弹"""

        super(AlienBullets, self).__init__()

        self.screen                =    ai_game.screen                        # 获取游戏屏幕

        self.screen_rect           =    ai_game.screen.get_rect()             # 获取游戏屏幕尺寸及位置

        self.settings              =    ai_game.settings                      # 获取游戏设置

        self.image                 =    image.load("images/alien_bullet_1.bmp")     # 获取子弹图像

        self.rect                  =    self.image.get_rect()                 # 获取子弹图像大小

        self.rect.midtop           =    alien.rect.midbottom                  # 将子弹上边沿居中对齐至外星人下边沿

        self.x,self.y              =    float(self.rect.x),float(self.rect.y) # 将子弹坐标存为浮点数


        self.speed_x    =  (ai_game.ship.rect.x - self.rect.x)/\
                                        self.screen_rect.width*self.settings.alien_speed_x*0.8


        self.speed_y               =    (ai_game.ship.rect.y - self.rect.y)/\
                                        self.screen_rect.height*self.settings.alien_speed_x*1.2
                                                                              # 计算子弹 Y 方向速度

    def update(self):

        self.x                    +=    self.speed_x                          # 更新 X 坐标浮点数

        self.y                    +=    self.speed_y                          # 更新 Y 坐标浮点数

        self.rect.x,self.rect.y    =    self.x,self.y                         # 更新 X,Y 坐标


class AlienFire(Thread):

    def __init__(self,ai_game):

        Thread.__init__(self)

        self.aliens   = ai_game.aliens

        self.settings = ai_game.settings

        self.shooting = False

        self.aliens   = ai_game.aliens

        self.bullets  = pygame.sprite.Group()

    def run(self) :

        """子弹发射间隔定时"""

        sleep(0.1)

        while True:

            self.shooting = True

            sleep(self.settings.alien_bullet_freq)



