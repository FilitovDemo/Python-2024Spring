x = set()

while len(x)<20:
    a = int(input('請輸入'))
    x.add(a)


#----------------------
x = set()

while len(x)<20:
    a = int(input('請輸入'))
    if a in x:
        print('請重新輸入')
    x.add(a)
