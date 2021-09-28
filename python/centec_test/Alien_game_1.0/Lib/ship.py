import  pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):

        """初始化飞船并设置其初始位置"""

        super(Ship, self).__init__()

        self.screen                                       = ai_game.screen

        self.settings                                     = ai_game.settings

        self.screen_rect                                  = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。

        self.image = pygame.image.load("images/ship.bmp")

        self.rect = self.image.get_rect()

        # 将新飞船放置在屏幕底部中央

        self.rect.midbottom = self.screen_rect.midbottom

        # 在新飞船的X、Y坐标中存储小数值 计算飞船在x轴方向的比例，距离下边界的位置

        # 此版本屏幕大小不变 故不需要计算比例

        self.x, self.scale_x = round(self.rect.x + self.rect.width/2,2), round((self.rect.x+ self.rect.width/2)/self.screen_rect.right,2)


        self.y, self.scale_y = self.rect.y ,round(self.screen_rect.bottom - self.rect.y - self.rect.height/2,2)

        # 移动标志位

        self.move_up,self.move_down,self.move_left,self.move_right= False,False,False,False

        # 改变移速标志位

        self.speed_up,self.speed_down = False,False

    def center_ship(self):

        """将飞船居中放置"""

        # 将新飞船放置在屏幕底部中央

        self.rect.midbottom = self.screen_rect.midbottom

        # 此版本屏幕大小不变 故不需要计算比例

        self.x, self.scale_x = round(self.rect.x + self.rect.width / 2, 2), round(
            (self.rect.x + self.rect.width / 2) / self.screen_rect.right, 2)

        self.y, self.scale_y = self.rect.y, round(self.screen_rect.bottom - self.rect.y - self.rect.height / 2, 2)

    def update_speed(self):

        """"根据按键调整飞船速度"""

        if self.speed_up:

            self.settings.ship_speed   += 0.05 if self.settings.ship_speed == 0 else 0.01

            self.speed_up = False

        elif self.speed_down:

            self.settings.ship_speed   -= 0    if self.settings.ship_speed - 0.01 < 0.04 else 0.01

            self.speed_down = False

        if self.settings.ship_speed < 0.05:

            self.settings.ship_speed = 0

    def update_move(self):

        """根据移动标志调整飞船位置"""

        # 更正飞船距离下边界的位置（self.scale_y）和 Y轴上的位置（self.y），

        if self.move_up or self.move_down:

            if self.move_up and self.rect.top > 0:

                self.y -= self.settings.ship_speed

            if self.move_down and self.rect.bottom < self.screen_rect.bottom:

                self.y += self.settings.ship_speed

        # 更正飞船在X轴上的位置（self.x） 和 飞船在X轴上的比例（self.scale.x）

        if self.move_right or self.move_left :

            if self.move_left and self.rect.left > 0:

                self.x -= self.settings.ship_speed

            if self.move_right and self.rect.right < self.screen_rect.right:

                self.x += self.settings.ship_speed

        # 根据飞船的位置（self.x，self.y），更新飞船在屏幕上的位置（self.rect.x，self.rect.y）

        self.rect.x = self.x

        self.rect.y = self.y

    def blit_me(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    """

    def update_scale(self):

        根据画面X轴的变动，更新飞船在X，Y上的位置

        此版本不需要调整比例

        if self.screen_rect != self.screen.get_rect():

            self.screen_rect = self.screen.get_rect()

            self.x = round(self.scale_x*self.screen_rect.right,2)

            self.y = round(self.screen_rect.bottom - self.scale_y - self.rect.height/2,2)
        
    def update_move(self):

        根据移动标志调整飞船位置

        # 更正飞船距离下边界的位置（self.scale_y）和 Y轴上的位置（self.y），

        if self.move_up or self.move_down:

            if self.move_up and self.rect.top > 0:

                self.scale_y += self.settings.ship_speed

            if self.move_down and self.rect.bottom < self.screen_rect.bottom:

                self.scale_y -= self.settings.ship_speed

            self.y = round(self.screen_rect.bottom - self.scale_y - self.rect.height/2,2)

        # 更正飞船在X轴上的位置（self.x） 和 飞船在X轴上的比例（self.scale.x）

        if self.move_right or self.move_left :

            if self.move_left and self.rect.left > 0:

                self.x -= self.settings.ship_speed

            if self.move_right and self.rect.right < self.screen_rect.right:

                self.x += self.settings.ship_speed

        #    self.scale_x = round(self.x/self.screen_rect.right,2)

        # 根据飞船的位置（self.x，self.y），更新飞船在屏幕上的位置（self.rect.x，self.rect.y）

        self.rect.x = round(self.x - self.rect.width/2,2)

        self.rect.y = self.y
    """

