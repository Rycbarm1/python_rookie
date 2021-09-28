import pygame

from time import sleep
from threading import Thread
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game,dic,speed_x,speed_y):

        """初始化外星人并设置起始位置"""

        super(Alien, self).__init__()

        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        # 加载图像 设置其rect属性

        self.image = pygame.image.load("images/alien.bmp")

        self.rect = self.image.get_rect()

        self.settings = ai_game.settings

        self.alien_speed_x = speed_x

        self.alien_speed_y = speed_y

        # 在（X，Y）位置 放置外星人

        if dic == 1:

            self.rect.x, self.rect.y = 0, 50

        if dic == 2:

            self.rect.x, self.rect.y = self.screen_rect.width - self.rect.width, 50
        # 存储外星人的精准坐标

        self.x, self.y = float(self.rect.x), float(self.rect.y)
        
        self.counts    = self.settings.alien_bullet_counts     # 初始化外星人子弹数

    def update(self):

        """根据设置速度移动外星人"""

        if self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left:

            self.alien_speed_x = -self.alien_speed_x

        self.x += self.alien_speed_x

        self.y += self.alien_speed_y

        self.rect.x, self.rect.y = self.x, self.y

class AlienShow(Thread):

    def __init__(self,ai_game):

        self.flag      =   False                       # 生成标志

        self.number    =   0                           # 生成波数

        self.settings  =   ai_game.settings            # 获取游戏设置（外星人生成频率）

        Thread.__init__(self)

    def run(self):

        """外星人生成间隔定时"""

        while True:

            if self.settings.alien_counts < 10:

                self.flag = True

                sleep(self.settings.alien_freq)

            else:
                return True
