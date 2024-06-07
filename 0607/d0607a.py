# map()
a = [10,20,30,40,50,60,70]

#b = [a的兩倍]

#方法1
b = []
for x in a:
    b.append(x*2)

#方法2
b = [x*2 for x in a]

#方法3  [] () {} 所有可迭代
def pp(x):
    return x*2

b = list(map(pp,a))

#方法3 縮短
b = list(map(lambda x:x*2,a))