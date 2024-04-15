x = input()    # 直接處理輸入的字串

# y = [int(a) for a in x.split()]

y = []
for a in x.split():
    y.append( int(a) )

print(y)