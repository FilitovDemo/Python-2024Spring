#不考慮效率
#印出使用者輸入數的質因數
x = int(input('請輸入整數'))

for a in range(1,x+1):
    if x%a==0:
        #a是x的因數
        #判斷a是否是質數
        c = 0   #a的因數個數
        for b in range(1,a+1):
            if a%b==0:
                c = c+1
        if c<=2:  #質數的因數只有兩個
            #a是質數
            print(a)