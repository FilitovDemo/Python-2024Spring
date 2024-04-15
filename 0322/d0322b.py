x = list()     # 等同 x = []

for _ in range(20):
    a = int(input('請輸入整數'))

    if a not in x:    #清單中如果沒有這個輸入值
        x.append(a)   #存到清單

#印出清單內容
#print(x)
for a in x:
    print(a)

#檢查某個值有沒有出現在x中
#if 999 in x:
#    print('清單中有999')

