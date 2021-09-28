from time import sleep
from threading import Thread

class Invincible(Thread):

    def __init__(self):

        Thread.__init__(self)

        self.flag = True

    def run(self):

        sleep(2)

        self.flag = True



