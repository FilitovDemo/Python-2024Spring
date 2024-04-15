x = []

for _ in range(30):
    a = int(input('請輸入整數'))
    x.append(a)
#-------------所有輸入值存到x清單
t = sum(x)
v = t/len(x)
ma = max(x)
mi = min(x)

print( f'總和{t}' )
print( f'平均{v}' )
print( f'最大值{ma}' )
print( f'最小值{mi}' )