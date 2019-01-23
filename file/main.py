import os

PATH = os.path.dirname(__file__) + '/test.txt'

def func():
    if os.path.exists(PATH):
        os.remove(PATH)
        print '%s removed.' % PATH
    else:
        print '%s not exists.' % PATH

if __name__ == '__main__':
    func()
