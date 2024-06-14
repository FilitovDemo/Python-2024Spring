#不考慮效率
#印出使用者輸入數的質因數

#取得x的所有正因數
def divisor(x):
    c = []
    for b in range(1,x+1):
        if x%b==0:
            c.append(b)
    return c

#判斷x是否是質數 (1)
def isPrime(x):
    c = 0
    for b in range(1,x+1):
        if x%b==0:
            c = c+1
    if c<=2:
        return True
    return False

#重用 resuse
#-------------------------

x = int(input('請輸入整數'))

for a in divisor(x):
    if isPrime(a):
        print(a)