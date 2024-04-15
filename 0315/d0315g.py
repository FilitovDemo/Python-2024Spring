# x = input('請輸入整數,多個整數的話以空白隔開')
# y = list(map(int,x.split()))

y = list(map(int,input('請輸入整數,多個整數的話以空白隔開').split()))

print(y)


for a in map(int,input('請輸入整數,多個整數的話以空白隔開').split()):
    print(a)


for a in input('請輸入整數,多個整數的話以空白隔開').split():
    print( int(a) )


# # m = x.split()
# # print(m)

# # # 對清單中的每個元素 "逐個" int
# # #逐個處理後的map物件 = map(處理,清單)
# # y = list(map(int,m))

# for b in y:
#     print(b)

# #print(y)

# # y = []
# # for a in m:
# #     y.append( int(a) )
# # print(y)