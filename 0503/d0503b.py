x = input('請輸入一段文字:')

# .split(分隔字串)
# .split() 預設是 空格 (不論個數)
# .split(',')  一個逗點  !!連續的兩個逗點會切成三分
# .split('===')
xx = x.split()

xx.reverse()

# for a in xx:
#     print(a, end=' ')
s = ''
for a in xx:
    s = s+a+' '

print(s)