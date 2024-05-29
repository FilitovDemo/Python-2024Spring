x = 100

def test1():
    global x              # 全域
    x = 200
    print('我在test1中:', x)

print('我在main中:', x)
test1()
print('我在main中:', x)   # 100? 200?

