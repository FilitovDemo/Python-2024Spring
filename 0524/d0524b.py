def test1(x):
    x = 200

def test2(y):      # 傳入一個清單作為參數
    y[0] = 200

x = 100
test1(x)
print(x)

mm = [100,300,500]
test2(mm)         # 複製過去的是清單的參考
print(mm)

pp = [100,300,500]
test2( pp[:] )     # 手動複製一份清單 通常不需要
print(pp)
