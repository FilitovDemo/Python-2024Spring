# 離開函數
# 1)執行完最後一句時
# 2)執行到return時離開
def test():
    print('aaa')
    print('bbb')
    return
    print('ccc')


print('呼叫前')
test()
print('呼叫後')