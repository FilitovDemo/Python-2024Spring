def add_left(x,a):
  x.insert(0,a)


def add_right(x,a):
  x.append(a)


def pop_left(x):
  if len(x)==0:
    return None
  return x.pop(0)


def pop_right(x):
  if len(x)==0:
    return None
  return x.pop()



x = [10]
add_left(x, 20)
print(x)
add_right(x, 30)
print(x)
a = pop_left(x)
print(a, x)
b = pop_right(x)
print(b, x)
c = pop_right(x)
print(c, x)
d = pop_left(x)
print(d, x)