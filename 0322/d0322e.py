#a = set([1,3,5,6,30,40])
a = {1,3,5,6,30,40}
b = {5,6,100,200}

#聯集
c = a.union(b)    # {1, 3, 100, 5, 6, 40, 200, 30}
c = a | b         # 唸做 or

#交集
d = a.intersection(b)    # {5, 6}
d = a & b                # 唸做 and

#差集 (?)
e = a.difference(b)      # {40, 1, 3, 30}
e = a - b
f = b.difference(a)      # {200, 100}
f = b - a

#對稱差集(?) 互斥或
e = a.symmetric_difference(b)  # {1, 3, 100, 200, 40, 30}
e = a ^ b                      # 唸做 xor
print(e)

