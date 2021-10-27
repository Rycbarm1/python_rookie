from time import time
from pygame import image

class Settings:

    """存储游戏设置的类"""

    def __init__(self):

        """初始化游戏设置"""


        self.bg_color            =   (230,230,230)                  # 屏幕颜色

        # self.screen_scale       =   int(ai_game.screen_width/ai_game.screen_height)
                                                                   # 获取屏幕比

        self.start_time          =   time()                         # 游戏开始时间

        self.run_time            =   0                              # 游戏运行时间

        self.ship_speed          =   0.5                            # 飞船速度

        self.ship_limit          =   3                              # 飞船生命值

        self.bullet_speed        =   0.7                            # 子弹速度

        self.bullet_freq         =   0.1                            # 子弹发射频率

        self.bullet_kind         =   0                              # 子弹种类

        self.bullet_width        =   3                              # 子弹宽度

        self.bullet_height       =   15                             # 子弹高度

        self.bullet_image        =   []

        self.bullet_image.append(image.load("images/bullet_1.bmp"))    #获取子弹图像

        self.bullet_image.append(image.load("images/bullet_2.bmp"))    #获取子弹图像

        self.bullet_image.append(image.load("images/bullet_3.bmp"))    #获取子弹图像

        self.bullet_image.append(image.load("images/bullet_4.bmp"))    #获取子弹图像

        self.alien_freq          =   0.3                            # 外星人生成频率

        self.alien_speed_x       =   0.2                            # 外星人x坐标速度

        self.alien_speed_y       =   0.1                            # 外星人y坐标速度

        self.alien_points        =   50                             # 外星人分数

        self.alien_counts        =   0                              # 生成外星人数量(计数)

        self.alien_bullet_counts =   10                             # 外星人子弹计数

        self.alien_bullet_freq   =   0.5                            # 外星人子弹发射频率
