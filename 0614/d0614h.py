def add(x,y):
    z = x+y
    return z


def main():
    m = add(100,200)
    print(m)


# 如果我是自己執行的
# 如果我是被import甚麼也不能做
if __name__=='__main__':
    main()
