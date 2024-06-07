a = [3,5,7,9,4,8,6,2,1]

#改成由大排到小
#b = sorted(a, reverse=True)

#由小到大 反過來
# b1 = sorted(a)
# b = b1[::-1]

#加負號 由小到大 加負號(負負得正)轉回來
# b1 = [-x for x in a]
# b2 = sorted(b1)
# b = [-x for x in b2]

#指定 判斷順序的值 實際上落座的還是原來的值
def pp(x):
    return -x

b = sorted(a, key=pp)

#用lambda縮短
b = sorted(a, key=lambda x:-x)

print(b)