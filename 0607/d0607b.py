#lambda 
#匿名函數
def pp(x):
    return x*2

lambda x: x*2
#-------------------
def test(i):
    return i**3

lambda i: i**3
#-------------------
def add(a,b):
    return a+b

lambda a,b:a+b
#-------------------
def 名字不重要(參數):
    return 回傳值

lambda 參數:回傳值

#----------------
def exam(x):
    if x%2==1:
        return True
    else:
        return False

lambda x:True if x%2==1 else False