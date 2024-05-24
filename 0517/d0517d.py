def mymax(a,b):
    if a>=b:
        return a
    else:
        return b


def mymax2(a,b):
    if a>=b:
        return a
    return b


x = mymax(100,200)
print(x)

print( mymax(50,30) )

#      __________________________________
print( mymax( mymax(10,30), mymax(20,5) ) )
#print( mymax( 30         , mymax(20,5) ) )
#print( mymax( 30         , 20          ) )
#print( 30                                )