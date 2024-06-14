from d0614c import add
from d0614c import divisor,isPrime
#from d0614c import *

x = add(10,20)

print(x)


x = int(input('請輸入整數'))

for a in divisor(x):
    if isPrime(a):
        print(a)