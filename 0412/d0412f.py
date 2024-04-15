x = [3,5,7,9,4,5,3,2,1,5,3,4,2,7]

# x 裡有幾個奇數 及幾個偶數?

c = 0

for a in x:
    if a%2==1:
        c = c+1

print('奇數', c, '個')

e = 0

for a in x:
    if a%2==0:
        e = e+1

print('偶數', e, '個')