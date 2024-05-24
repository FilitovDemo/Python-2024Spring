from collections import Counter
x = [3,2,4,2,1,5,8,5,7,6,9,7,5,2]

c = Counter(x)

# print('0出現',c[0],'次')
# print('1出現',c[1],'次')
# print('2出現',c[2],'次')

for k in c:
    print(k,'出現',c[k],'次')