x = list()     # 等同 x = []

for _ in range(20):
    a = int(input('請輸入整數'))
    x.append(a)


#清單裡面有值,想辦法去除重複的
y = set(x)   # 把清單x轉換成set

#印出清單內容
#print(y)         #????
#print( list(y) ) #????
for a in y:
    print(a)