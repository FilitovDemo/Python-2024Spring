x = [3,5,7,9,4,5,3,2,1,5,3,4,2,7]

# x 裡 0~9 出現幾次

c0 = 0    # 0出現的個數
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

for a in x:
    if a==0:
        c0 = c0+1
    elif a==1:
        c1 = c1+1
    elif a==2:
        c2 = c2+1
    elif a==3:
        c3 = c3+1
    elif a==4:
        c4 = c4+1
    elif a==5:
        c5 = c5+1
    elif a==6:
        c6 = c6+1
    elif a==7:
        c7 = c7+1
    elif a==8:
        c8 = c8+1
    elif a==9:
        c9 = c9+1

print('0出現', c0, '次')
print('1出現', c1, '次')
print('2出現', c2, '次')
print('3出現', c3, '次')
print('4出現', c4, '次')
print('5出現', c5, '次')
print('6出現', c6, '次')
print('7出現', c7, '次')
print('8出現', c8, '次')
print('9出現', c9, '次')