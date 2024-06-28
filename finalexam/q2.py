f = open('D:\\data.txt')

for a in f:
  if a[0]=='j':
    print(a, end='')

f.close()

#--------------------------
# for a in f:
#   a = a.strip()
#   if a[0]=='j':
#     print(a)
#--------------------------
# for a in f:
#   if a[0]=='j':
#     print(a.strip())


