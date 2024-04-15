x = [1,1,1,1,8,8,9,9,9,9,9,9,9,9,9]

# x 裡 0~9 出現幾次

#c = dict()
c = {}

# 讓 c[0]代表 0出現的個數
# 讓 c[1]代表 1出現的個數
#....c[9]代表 9出現的個數

for a in x:
    #a可能尚未出現過 所有 c[a]還不存在
    if a not in c:   # 用 c.get(a) 可以省略這部分
        c[a] = 0

    c[a] = c[a]+1


for i in c:
    print(i, '出現', c[i], '次')
