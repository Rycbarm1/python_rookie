from pygame import font

from pygame.sprite import Group
from Lib.ship import Ship

class Scoreboard:

    """显示得分信息的类"""

    def __init__(self,ai_game):

        """初始化显示得分涉及的属性"""

        font.init()

        self.ai_game =  ai_game

        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        self.settings =ai_game.settings

        self.stats  =ai_game.stats

        self.ships = Group()

        #  显示得分信息时使用的字体设置

        self.text_color = (30,30,30)

        self.font  = pygame.font.Font('ALL.otf',48)

        # 初始化得分图像

        self.prep_score()

        self.prep_high_score()

        self.prep_ships()

    def prep_score(self):

        """将得分转换为一副渲染的图像"""

        score_str = round(self.stats.score)

        score_str = '{:,}'.format(score_str)

        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # 在屏幕右上角显示得分

        self.score_rect  = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 20

        self.score_rect.top = 20

    def prep_high_score(self):

        """将最高得分转换为一副渲染的图像"""

        high_score = round(self.stats.high_score,-1)

        high_score_str ='{:,}'.format(high_score)

        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        # 在屏幕右上角显示得分

        self.high_score_rect  = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx

        self.high_score_rect.bottom = self.score_rect.bottom

    def check_high_score(self):

        """检查是否生成最高得分"""

        if self.stats.score > self.stats.high_score:

            self.stats.high_score  =  self.stats.score

            self.prep_high_score()

    def show_score(self):

        """在屏幕上显示得分"""

        self.screen.blit(self.score_image,self.score_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.ships.draw(self.screen)

    def prep_ships(self):

        """显示还余下多少飞船"""

        self.ships.empty()

        for ship_number in range(self.stats.ships_left):

            ship = Ship(self.ai_game)

            ship.rect.x = 20+ship_number*ship.rect.width

            ship.rect.y = 20

            self.ships.add(ship)
