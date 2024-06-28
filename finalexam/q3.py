x = int(input('請輸入整數：'))

print('質因數分解為：')

a = 2
while a<=x:
  if x%a==0:
    print(a)
    x = x//a
  else:
    a = a+1

#--------------------------
# print('質因數分解為：')
#
# for a in (2,3,5,7):
#   while x%a==0:
#     print(a)
#     x = x//a
#
# if x>1:
#   print(x)

#--------------------------
# dvsr = []
# a = 2
# while a<=x:
#   if x%a==0:
#     dvsr.append( str(a) )
#     x = x/a
#   else:
#     a += 1
#
# print('質因數分解為：' + ','.join(dvsr) )