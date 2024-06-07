a = [ [3,2],
      [3,1],
      [2,3],
      [2,1],
      [2,2]  ]

# 第一個數字由大到小  第二個數字由小到大
# def pp(x):
#     return (-x[0],x[1])

# b = sorted(a, key=pp)


# 先排第2個數字 再排第1個數字
# def pp(x):
#     return (x[1],x[0])

# b = sorted(a, key=pp)

# 只排第2個數字 第1個數字無所謂
def pp(x):
     return x[1]

b = sorted(a, key=pp)

print(b)