def func(x, y, z):
    print(f'{x}, {y}, {z}')

    if y:
        print('y is exists')

    if not y:
        print('y is not exists')

if __name__ == '__main__':
    func('test1', None, 'test3')
