# x = [int(a) for a in input('請輸入多個整數').split(' ')]
# x = map(int, input('請輸入多個整數').split(' '))
# x = list(map(int, input('請輸入多個整數').split(' ')))

#--------------------------

s = input('請輸入多個整數 用空白隔開')
xx = s.split(' ')

# x = []
# for a in xx:
#     x.append( int(a) )

# x = [int(a) for a in xx]

# x = list(map(int, xx))

x = map(int, xx)   #對照 映射 一對一對應 逐個處理

