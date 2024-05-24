def test():
    #print('函數內部的程式碼')
    return 100


def add(x, y):
    z = x+y
    return z


a = add(100,50)
b = add(10,20)
print(a)
print(b)
print( add(100,200) )
print( add(add(10,20),30) )