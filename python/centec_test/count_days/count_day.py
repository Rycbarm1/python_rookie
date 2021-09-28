# -*-coding:utf-8-*-
# from shutil import copyfile
# import os, re, time

class DateCount:

    def __init__(self):

        self.year = 0
        self.mon  = 0
        self.day  = 0
        self.days = 0

    def get_order(self, limit):

        while True:

            data = int(input("请输入年份："))

            if limit < data:

                print("---error：please resume load")

            else:

                break

        self.year = int(input("请输入年份："))
        print(self.year)
        self.mon = int(input("请输入月份："))
        print(self.mon)
        self.day = int(input("请输入月份："))
        print(self.day)

    def count(self):

        self.days += self.day

        for mon in range(1 , self.mon):

            self.days += 31

            if mon < 8:

                if mon % 2 == 0:

                    self.days -= 1

            else:

                if mon % 2 == 1:

                    self.days -= 1

        if ((self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0) and self.mon > 2:

            self.days -= 1

        elif self.mon > 2:

            self.days -= 2

        print(self.days)

    def main(self):

        self.get_order()
        self.count()


if __name__ == "__main__":
    
    date = DateCount()
    date.main()
