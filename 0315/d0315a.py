# []
# 輸入 10      [10]
# 輸入 20      [10,20]      往右邊放
# 輸入 50      [10,20,50]
x = [int(input('請輸入整數:')) for _ in range(20)]

#從清單的右邊,印到左邊
for i in range(19,-1,-1):
    print( x[i] )

# for i in range(20,0,-1):
#     print( x[i-1] )

# i = 19
# while i>=0:
#     print( x[i] )
#     i = i-1

# print( x[19] )
# print( x[18] )
# print( x[17] )
# print( x[16] )
# print( x[15] )
# print( x[14] )
# print( x[13] )
# print( x[12] )
# print( x[11] )
# print( x[10] )
# print( x[9] )
# print( x[8] )
# print( x[7] )
# print( x[6] )
# print( x[5] )
# print( x[4] )
# print( x[3] )
# print( x[2] )
# print( x[1] )
# print( x[0] )
