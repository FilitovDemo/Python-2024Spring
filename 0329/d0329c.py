x = []
c = 0
while c<20:
    a = int(input('請輸入'))
    if a not in x:   #如果a不在清單中 加入到清單中
        x.append(a)
        c = c+1
    else:            #或者(a在清單中)
        print('請重新輸入')

#----------------------------------
x = []

while len(x)<20:
    a = int(input('請輸入'))
    if a not in x:   #如果a不在清單中 加入到清單中
        x.append(a) 
    else:            #或者(a在清單中)
        print('請重新輸入')

