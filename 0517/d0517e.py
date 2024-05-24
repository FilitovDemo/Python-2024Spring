# x = [10,20,30,40,50]
# v = sum(x)
# print(v)

# x = [10,20,30,40,50]
# v = 0
# for a in x:
#     v = v+a
# print(v)

def sumOf2(oooxxx):
    t = sum(oooxxx)
    return t


def sumOf(oooxxx):
    t = 0
    for a in oooxxx:
        t = t+a
    #t裡面存的是oooxxx的總和,回傳
    return t


x = [10,20,30,40,50]
v = sumOf(x)
print(v)

print( sumOf([20,30,50,68]) )
