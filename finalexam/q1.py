w,h = map(int,input('請輸入寬與高：').split(','))

for _ in range(h):
    print('*'*w)

#--------------------------
# s = input('請輸入寬與高：')
# xs = s.split(',')
# w = int(xs[0])
# h = int(xs[1])
#--------------------------
# xs = input('請輸入寬與高：').split(',')
# w = int(xs[0])
# h = int(xs[1])
#--------------------------
# xs = input('請輸入寬與高：').split(',')
# xs2 = map(int,xs)
# w = xs2[0]
# h = xs2[1]
#--------------------------
# xs2 = map(int,input('請輸入寬與高：').split(','))
# w = xs2[0]
# h = xs2[1]
#--------------------------
# w,h = map(int,input('請輸入寬與高：').split(','))
#==========================
# for _ in range(h):
#     print('*'*w)
#--------------------------
# for _ in range(h):
#     for j in range(w):
#         print('*',end='')
#--------------------------
# print( ('*'*w+'\n')*h )
#--------------------------