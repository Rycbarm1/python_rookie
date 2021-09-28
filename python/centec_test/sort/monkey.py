
import random
import time


def monkey_sort(monkey_sort_list):

    for monkey_sort_loop in range(len(monkey_sort_list)):

        change_sub = random.randint(0, len(monkey_sort_list)-1)
        monkey_sort_list[monkey_sort_loop], monkey_sort_list[change_sub] = monkey_sort_list[change_sub], monkey_sort_list[monkey_sort_loop]


def is_right(is_right_list):

    for is_right_loop in range(len(is_right_list) - 1):

        if is_right_list[is_right_loop] > is_right_list[is_right_loop + 1]:

            return False

    return True


def init_list():

    while True:
        try:
            init_list_num = int(input('请输入初始列表长度：'))
        except:
            print('wrong num')

        else:
            break

    init_list_list = []

    for init_list_loop in range(init_list_num):

        init_list_list.append(init_list_loop + 1)

    random.shuffle(init_list_list)

    return init_list_list


if __name__ == "__main__":

    a = init_list()
    print('初始列表：{}'.format(a))
    count = 1

    while True:
        monkey_sort(a)
        print('\r第 {} 次排序，排序结果：{}'.format(count, a), end='')
        if is_right(a):
            break
        count += 1

    print('\n共排序{}次'.format(count))
