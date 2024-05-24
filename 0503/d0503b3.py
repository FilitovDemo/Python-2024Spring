# x1 = input('請輸入一段文字:')   #輸入
# x2 = x1.split()    #切割
# x3 = x2[::-1]      #倒序
# x4 = ' '.join(x3)   #組合
# print(x4)            #印出

print(' '.join(input('請輸入一段文字:').split()[::-1]))