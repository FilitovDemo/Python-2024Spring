a = int(input('請輸入整數'))
b = int(input('請輸入整數'))
c = int(input('請輸入整數'))

x = [a,b,c]
#---------------------------
t = sum(x)
v = t/len(x)
ma = max(x)
mi = min(x)

print( f'總和{t}' )
print( f'平均{v}' )
print( f'最大值{ma}' )
print( f'最小值{mi}' )