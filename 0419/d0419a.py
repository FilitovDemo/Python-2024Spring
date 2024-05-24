# dict
s = 'this is a book'

#s.replace(' ','')
for a in s:
    #if a==' '
    #if a.isalpha()
    #if a>='a' and a<='z'
    #if a in ('a','b','c','d','e','f')
    if a in 'abcdefghijlmnop'



#c = {}
c = dict()

for a in s:
    c[a] = c.get(a,0) + 1
    # if a in c:
    #     c[a] = c[a] + 1
    # else:
    #     c[a] = 0    + 1

for a in c:
    print(a, c[a])



# #有名字 的 清單
# c = {'a':0, 'b':0, 'c':0, 'd':0}
# c['a'] a字母出現的次數
# c['b'] b字母出現的次數
# c['m']

# x = [0,0,0,0.....]
# x[0] a字母出現的次數
# x[1] b字母出現的次數
# x[???]     m


# #屬性 / 值    key-value
# alice = {'國文':10, '英文':20, '總分':30}
# bob = {'國文':50, '英文':70, '總分':120}
# total = alice['國文'] + bob['國文']


# p1 = {'x':50,'y':20}
# p2 = {'x':0, 'y':0}
# p3 = {'x':20,'y':50}

# p = {'x':25, 'y':40}





#     0  1  2  3
#    -4 -3 -2 -1
#x = [10,20,30,40]
#x[1]
#x[-2]      x[位置]   x[索引]   x[平移]


# 不要只是數字 文字
# x[代號]   x[名稱]  x[key]  x[索引]   map  字典
#y = {'國文':10, '英文':20, '數學':30, '理化':40, 10:99, 0:10}
# y['國文']
# y['數學']
# y[10]
# y[0]