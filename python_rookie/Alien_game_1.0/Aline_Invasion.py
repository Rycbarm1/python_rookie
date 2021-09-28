import time
import sys
import pygame

from Lib.Settings     import Settings
from Lib.ship         import Ship
from Lib.key          import Key
from Lib.bullets      import Bullet, Fire
from Lib.alien        import Alien, AlienShow
from Lib.GameStats    import GameStats
from Lib.button       import Button
from Lib.socreboard   import Scoreboard
from Lib.alienbullets import AlienBullets, AlienFire


class Invasion:

    """管理游戏资源和行为"""

    def __init__(self):

        """初始化 并 创建游戏"""

        pygame.init()

        pygame.display.set_caption("Alien Invasion")

        # 初始化游戏并创建游戏资源

        self.settings          = Settings()                              # 获取游戏设置

        self.pc_screen         = pygame.display.Info()                   # 获取屏幕大小

        self.screen_width      = int(self.pc_screen.current_w/3.3)       # 设置游戏窗口宽度

        self.screen_height     = int(self.pc_screen.current_h*896/1080)  # 设置游戏窗口高度

                                                                         # 游戏窗口初始化
        self.screen            = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.stats             = GameStats(self)                         # 初始化游戏统计信息

        self.ship              = Ship(self)                              # 初始化飞船

        self.key               = Key(self)                               # 初始化游戏按键

        self.bullets           = pygame.sprite.Group()                   # 初始化子弹组

        self.fire              = Fire(self)                              # 初始化子弹发射间隔时间的线程

        self.aliens            = pygame.sprite.Group()                   # 初始化外星人组

        self.aliens_1          = pygame.sprite.Group()                   # 初始化外星人组

        self.alien_show        = AlienShow(self)                         # 设置外星人出现间隔时间的线程

        self.aliens_bullets    = pygame.sprite.Group()                   # 初始化外星人子弹

        self.alien_fire        = AlienFire(self)                         # 初始化外星人发射子弹间隔时间的线程

        try:

            self.play_button       = Button(self, 'Play')                 # 创建游戏按键

            self.sb                = Scoreboard(self)                    # 创建游戏记分板

        except:

            print('error')

    def _update_key(self):

        """检测键盘和鼠标状态"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                self.key.mouse_down(event)

                mos_pos = pygame.mouse.get_pos()

                self._update_button(mos_pos)

            elif event.type == pygame.MOUSEBUTTONUP:

                self.key.mouse_UP(event)

            elif event.type == pygame.KEYDOWN:

                self.key.key_down_event(event)

            elif event.type == pygame.KEYUP:

                self.key.key_up_event(event)

            self.key.update_keyword()

    def _update_button(self,mos_pos):

        """更新游戏内按钮信息"""

        if self.key.mouse_left and self.play_button.rect.collidepoint(mos_pos):

            self.stats.reset_stats()

            self.sb.prep_score()

            self.stats.game_active = True

            self.clear_screen()

    def _update_ship(self):

        """更新飞船速度和位置"""

        self.ship.update_speed()

        # 此版本不需调整窗口大小
        # self.ship.update_scale()

        self.ship.update_move()

    def _update_bullets(self):

        self.bullets_fire()

        self.bullets_qty()

    def _update_aliens(self):

        self.alien_show_()

        self.alien_qty()

        self.alien_move()

        self.kill_alien()

        self.alien_bullets()

    def _update_alien_bullets(self):

        """更新外星人子弹"""

        self.alien_bullets()

        self.alien_bullets_move()

    def bullets_fire(self):

        """更新子弹发射标志"""

        if self.key.fire and not self.fire.is_alive():

                self.fire.setDaemon(True)

                self.fire.start()

        elif not self.key.fire and self.fire.is_alive():

            self.fire = Fire(self)

    def bullets_qty(self):

        """更新子弹数量"""

        if self.fire.shooting :

            self.fire.shooting = False

            new_bullet = Bullet(self,self.settings.bullet_image[self.settings.bullet_kind])

            self.bullets.add(new_bullet)

    def bullets_draw(self):

        """更新子弹位置"""

        self.bullets.update()

        self.bullets.draw(self.screen)

        for bullet in self.bullets.copy():

            if bullet.rect.bottom < 0:

                self.bullets.remove(bullet)

    def alien_show_(self):

        """更新外星人出现标志"""

        if len(self.aliens) + len(self.aliens_1) == 0 or self.settings.alien_counts == 5 :

            self.alien_show = AlienShow(self)

        if len(self.aliens) + len(self.aliens_1) == 0 and \
                (self.settings.alien_counts == 5 or self.settings.alien_counts == 0):

            self.alien_show.setDaemon(True)  # 守护外星人出现的线程

            self.alien_show.start()  # 启动外星人出现线程

            if not self.alien_fire.is_alive():

                self.alien_fire.setDaemon(True)  # 守护外星人发射子弹的线程

                self.alien_fire.start()

            self.settings.alien_counts = 0

    def alien_qty(self):

        """更新外星人数量"""

        if self.alien_show.flag :

            self.settings.alien_counts +=  1

            self.alien_show.flag    = False

            new_alien = Alien(self, 1, self.settings.alien_speed_x, self.settings.alien_speed_y)

            self.aliens.add(new_alien)

            new_alien = Alien(self, 2, -self.settings.alien_speed_x, self.settings.alien_speed_y)

            self.aliens.add(new_alien)

    def alien_move(self):

        """移动外星人"""

        self.aliens.update()

        self.aliens_1.update()

        for alien in self.aliens.copy():

            if alien.rect.top > self.screen.get_rect().bottom:

                self.aliens.remove(alien)

        for alien in self.aliens_1.copy():

            if alien.rect.top > self.screen.get_rect().bottom:

                self.aliens_1.remove(alien)

        if pygame.sprite.spritecollideany(self.ship,self.aliens) or \
           pygame.sprite.spritecollideany(self.ship,self.aliens_1):

            self._ship_hit()

    def kill_alien(self):

        """检测外星人和子弹的碰撞"""

        aliens = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if aliens:

            # for alien in aliens:

            #     self.aliens_1.add(aliens[alien])

            #     self.aliens.remove(aliens[alien])

            self.stats.score += self.settings.alien_points

            self.sb.prep_score()

            self.sb.check_high_score()

        # if pygame.sprite.group_collide(self.bullets, self.aliens_1, True, True):  此处当外星人需要二次射击消灭时启用

    def aliens_draw(self):

        """更新外星人位置"""

        self.aliens.draw(self.screen)

        self.aliens_1.draw(self.screen)

    def alien_bullets(self):

        """使每个外星人发射子弹"""

        flag = True

        for alien in self.aliens:

            if alien.counts > 0:

                flag = False

                if self.alien_fire.shooting:

                    alien.counts -= 1

                    alien_bullet = AlienBullets(self, alien)

                    self.aliens_bullets.add(alien_bullet)

        self.alien_fire.shooting = False

        print(f'\r{len(self.aliens_bullets)}  {flag}  {self.settings.alien_counts}',end='')

        if flag and self.settings.alien_counts == 10:

            self.alien_fire = AlienFire(self)

    def alien_bullets_move(self):

        """移动外星人子弹"""

        self.aliens_bullets.update()

        for bullet in self.aliens_bullets.copy():

            if bullet.rect.top > self.screen.get_rect().bottom \
                or bullet.rect.right < self.screen.get_rect().left\
                 or bullet.rect.left > self.screen.get_rect().right :

                self.aliens_bullets.remove(bullet)

        if pygame.sprite.spritecollideany(self.ship,self.aliens_bullets):

            self._ship_hit()

    def _ship_hit(self):

        """响应飞船被外星人撞到"""

        if self.stats.ships_left > 1:

            self.stats.ships_left -= 1

            time.sleep(0.5)

            self.sb.prep_ships()

            self.clear_screen()

        else:

            self.stats.game_active = False

            time.sleep(0.5)

    def clear_screen(self):

        self.bullets.empty()           # 清空余下的子弹

        self.aliens.empty()            # 清空余下的外星人

        self.aliens_bullets.empty()    # 清空余下的外星人子弹

        self.ship.center_ship()        # 将飞船放至屏幕底部中央

        self.settings.alien_counts = 0 # 外星人计数为 0

        self.sb.prep_ships()

    def update_screen(self):

        self.screen.fill(self.settings.bg_color)

        self.ship.blit_me()

        self.bullets_draw()

        self.aliens_draw()

        self.aliens_bullets.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:

            self.play_button.draw_button()

        pygame.display.update()

    def run_game(self):

        """游戏主循环"""

        while True:

            self.settings.run_time = time.time() - self.settings.start_time

            self._update_key()

            if self.stats.game_active:

                pygame.mouse.set_visible(False)

                self._update_ship()

                self._update_bullets()

                self._update_aliens()

                self._update_alien_bullets()

            else:

                pygame.mouse.set_visible(True)

            self.update_screen()


if __name__ == '__main__':

    """创建游戏实例并运行"""

    ai = Invasion()

    ai.run_game()



    """搁置飞船无敌提案
    
    self.dam               =   Invincible()                           # 初始化无敌时间

    def ship_dam(self):

        self.dam = Invincible()

        self.dam.flag = False

        self.dam.setDaemon(True)

        self.dam.start()

    """

