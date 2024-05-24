def test():
    print('something')
    x = 100
    x = x+10
    print(x)


def twice(x):
    x = x*2
    print(x)


def mymax(x,y,z):
    m = max(x,y,z)
    print(m)


def test2(x):
    print('aaaa')
    if x<10:
        print('bbbb')


def test3(x):
    print('aaaa')
    if x>=10:
        return
    print('bbbb')


test2(5)
print('分隔')
test3(5)