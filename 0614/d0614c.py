def add(x,y):
    z = x+y
    return z

def print(x):
    print(f'>>>{x}<<<')

#判斷x是否是質數 (1)
def isPrime(x):
    c = 0
    for b in range(1,x+1):
        if x%b==0:
            c = c+1
    if c<=2:
        return True
    return False


#判斷x是否是質數 (2)
def isPrime2(x):
    c = divisor(x)
    if len(c)<=2:
        return True
    return False


#取得x的所有正因數
def divisor(x):
    c = []
    for b in range(1,x+1):
        if x%b==0:
            c.append(b)
    return c