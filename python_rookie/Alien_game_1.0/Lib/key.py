import pygame

from sys import exit

class Key:

    """ 存储游戏的所有按键标志"""

    def __init__(self,ai_game):

        self.ship                  = ai_game.ship

        self.settings              = ai_game.settings

        self.mouse_left            = False

        self.mouse_right           = False

        self.mouse_pos             = None

        self.up,    self.w         = False,False

        self.down,  self.s         = False,False

        self.left,  self.a         = False,False

        self.right, self.d         = False,False

        self.k                     = False

        self.space                 = False

        self.lshift                = False

        self.fire                  = False

        self.bullet_kind_add       = True

    def key_down_event(self,event):

        """响应按键"""

        if event.key == pygame.K_UP:

            self.up = True

        elif event.key == pygame.K_DOWN:

            self.down= True

        elif event.key == pygame.K_LEFT:

            self.left = True

        elif event.key == pygame.K_RIGHT:

            self.right = True

        if event.key == pygame.K_w:

            self.w = True

        if event.key == pygame.K_s:

            self.s = True

        if event.key == pygame.K_a:

            self.a = True

        if event.key == pygame.K_d:

            self.d = True

        if event.key == pygame.K_k:

            self.k = True

        if event.key == pygame.K_LSHIFT:

            self.lshift = True

        elif event.key == pygame.K_SPACE:

            self.space = True

        # elif event.key ==

    def key_up_event(self, event):

        """响应松开"""

        if event.key == pygame.K_UP:

            self.up = False

        elif event.key == pygame.K_DOWN:

            self.down = False

        elif event.key == pygame.K_LEFT:

            self.left = False

        elif event.key == pygame.K_RIGHT:

            self.right = False

        if event.key == pygame.K_w:

            self.w = False

        elif event.key == pygame.K_s:

            self.s = False

        elif event.key == pygame.K_a:

            self.a = False

        elif event.key == pygame.K_d:

            self.d = False

        elif event.key == pygame.K_k:

            self.k = False

        if event.key == pygame.K_LSHIFT:

            self.lshift = False

        elif event.key == pygame.K_SPACE:

            self.space = False

        elif event.key == pygame.K_q:

            exit()

    def mouse_down(self,event):

        if event.button == 1:

            self.mouse_left = True

        elif event.button == 3:

            self.mouse_right = True

    def mouse_UP(self,event):

        if event.button == 1:

            self.mouse_left = False

        elif event.button == 3:

            self.mouse_right = False

    def update_keyword(self):

        """根据按键调整相应的标志位"""

        self.ship.move_up    = (self.up or self.w) and not self.lshift

        self.ship.move_down  = (self.down or self.s) and not self.lshift

        self.ship.move_left  = (self.left or self.a) and not self.lshift

        self.ship.move_right = (self.right or self.d) and not self.lshift

        self.ship.speed_up   = self.up and self.lshift

        self.ship.speed_down = self.down and self.lshift

        self.fire            = self.space

        if self.k and self.bullet_kind_add:

            self.bullet_kind_add  =  False

            self.settings.bullet_kind += 1

            if self.settings.bullet_kind == 4:

                self.settings.bullet_kind = 0

        elif not self.k:

            self.bullet_kind_add = True




