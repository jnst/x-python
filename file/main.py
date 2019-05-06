import os


def func(path):
    if os.path.exists(path):
        os.remove(path)
        print(f'{path} removed.')
    else:
        print(f'{path} not exists.')


if __name__ == '__main__':
    path = os.path.dirname(__file__) + '/test.txt'
    func(path)
