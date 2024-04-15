x = set()    #不重複 (集合)

for _ in range(20):
    a = int(input('請輸入整數'))

    x.add(a)   #加入到set裡
               #set本來就不會重複
               #重複值直接排除
#印出清單內容
#print(x)
for a in x:
    print(a)

#檢查某個值有沒有出現在x中
#if 999 in x:
#    print('清單中有999')