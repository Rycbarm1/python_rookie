import pygame
from threading import Thread

class Screen(Thread):

    def __init__(self,ai_game):

        Thread.__init__(self)

        self.screen = ai_game.screen

        self.ship   = ai_game.ship

        self.settings = ai_game.settings

    def run(self):

        while True:

            print(" \r 飞船速度 ：",self.settings.ship_speed,end = '')

            pygame.display.flip()