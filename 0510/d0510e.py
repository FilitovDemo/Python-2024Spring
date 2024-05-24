def printMax(a, b, c):
    #x = max(a,b,c)
    # if a>b and a>c:
    #     x = a
    # elif b>c:
    #     x = b
    # else:
    #     x = c
    x = a
    if b>x:
        x = b
    if c>x:
        x = c
    print(x)


printMax(10,50,30)
printMax(500,20,150)
printMax(30,40,80)
printMax(99,99,99)