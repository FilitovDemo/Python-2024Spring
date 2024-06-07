a = [10,20,30,40]

#複製清單
#p = []                          # p = [x for x in a]
#for x in a:
#    p.append(x)

#p = a[:]                        # 清單[開始:結束:步進]

#替清單取別名  a 及 p 記住的都是同一個清單
#p = a


print('p:', p)
print('a:', a)

a[1] = 2000

print('p:', p)
print('a:', a)
