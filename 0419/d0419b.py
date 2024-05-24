# dict

c = {'apple':10, 'banana':20, 'cat':15}

print(c.items())

for k,v in c.items():
    print(k, v)

print( c.keys() )

for k in c.keys():
    print(k, c[k])

for k in c:
    print(k, c[k])

print( c.values() )