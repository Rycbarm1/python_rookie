import os


src_dir = "/Users/BAD/PycharmProjects/pythonProject/centec_test/lib/python3.8/site-packages/pip/_internal"


class Test:

    def __init__(self, src=os.getcwd(), need=None, no_need=None):

        self.need = [] if need is None else need
        self.no_need = [] if no_need is None else no_need

        self.src_dir = src
        self.file = []

    def get_file(self):

        for root, dirs, files in os.walk(self.src_dir):

            for file in files:

                ext = os.path.splitext(file)

                if (ext[1] in self.need or self.need == 'all') and (ext[1] not in self.no_need):

                    self.file.append(root+'/'+file)


if __name__ == "__main__":

    test = Test(src=src_dir, need='all')
    test.get_file()

    for file in test.file:
        print(file)
