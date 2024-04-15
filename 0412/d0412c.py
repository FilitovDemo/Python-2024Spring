s = input('輸入一行多個整數')
xx = s.split(' ')
for s in xx:
    a = int(s)
    #處理 a
    #print(a)


for s in input('輸入一行多個整數').split(' '):
    a = int(s)
    #處理 a
    #print(a)


for a in map(int,input('輸入一行多個整數').split(' ')):
    #處理 a
    #print(a)