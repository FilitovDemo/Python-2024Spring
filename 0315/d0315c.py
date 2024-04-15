# []
# 輸入 10         [10]
# 輸入 20      [20,10]      往左邊放
# 輸入 50   [50,20,10]

x = []                 #   x = list()

for _ in range(20):
    a = int(input('請輸入整數:'))
    x.insert(0, a)         # 最左邊是第0個位置,往清單的左邊(開始端)放


# 從左而右印出清單
for a in x:
    print( a )

# for i in range(20):
#     print( x[i] )

# i = 0
# while i<20:
#     print( x[i] )
#     i = i+1
