import pygame

from time import sleep
from threading import Thread
from pygame.sprite import Sprite

class Bullet(Sprite):

    """管理发出的所有子弹"""

    def __init__(self,ai_game,bullet_image):

        """在飞船当前位置创建子弹"""

        super(Bullet, self).__init__()

        self.screen                      =   ai_game.screen                  # 获取游戏屏幕

        self.screen_rect                 =   ai_game.screen.get_rect()       # 获取游戏屏幕尺寸及位置

        self.settings                    =   ai_game.settings                # 获取游戏设置

        self.image                       =   bullet_image                    # 获取子弹图像

        self.rect                        =   self.image.get_rect()           # 获取子弹图像大小

        self.rect.midbottom              =   ai_game.ship.rect.midtop        # 将子弹下边沿居中对齐至飞船上边沿

        self.y                           =   float(self.rect.y)              # 将子弹 Y 坐标转换为浮点数

    def update(self):

        """向上移动子弹"""

        self.y                          -= self.settings.bullet_speed         # 更新 Y 坐标浮点数

        self.rect.y                      = self.y                             # 更新 Y 坐标

class Fire(Thread):

    def __init__(self,ai_game):

        Thread.__init__(self)

        self.shooting                    =   False                            # 开火标志

        self.shooting_flag               =   False

        self.settings                    =   ai_game.settings                 # 获取游戏设置（子弹发射频率）

    def run(self):

        """子弹发射间隔定时"""

        while True:

            self.shooting = True

            sleep(self.settings.bullet_freq)








