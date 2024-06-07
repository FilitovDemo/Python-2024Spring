a = [3,5,7,9,4,8,6,2,1]

#由小到大 偶數排前面 奇數排後面
#b = [2,4,6,8,1,3,5,7,9]

#[3,5,7,9,4,8,6,2,1]
#[ [奇數,3],[奇數,5],[奇數,7],
#  [奇數,9],[偶數,4],[偶數,8],
#  [偶數,6],[偶數,2],[奇數,1]  ]
#[ [1,3],[1,5],[1,7],
#  [1,9],[0,4],[0,8],
#  [0,6],[0,2],[1,1]  ]
def pp(x):
    if x%2==1:
        return [1,x]
    else:
        return [0,x]
    
# def pp(x):
#     return [x%2,x]

b = sorted(a, key=pp)

#--------------------
b = sorted(a, key=lambda x:[1,x] if x%2==1 else [0,x])  #一樣
b = sorted(a, key=lambda x:[x%2,x])                     #一樣
b = sorted(a, key=lambda x:(1,x) if x%2==1 else (0,x))  #一樣 稍快
b = sorted(a, key=lambda x:(x%2,x))                     #一樣 稍快

print(b)










#篩出偶數,排序
#篩出奇數,排序
#合併
# m = sorted([x for x in a if x%2==0])
# n = sorted([x for x in a if x%2==1])
# b = m + n
