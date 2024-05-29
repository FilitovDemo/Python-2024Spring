def test1(x):
    print('我在test1:',x)
    test2(x)                   # OK
    print('我回到test1:',x)

test2(100)                     # ERROR

def test2(x):
    print('我在test2:',x)


test1(100)
