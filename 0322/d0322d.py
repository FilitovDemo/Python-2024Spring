a = set([1,3,5,6,30,40])
print(a)                   # {1, 3, 5, 6, 40, 30}
# 把 100 加入 a 裡面
a.add(100)                 # {1, 3, 100, 5, 6, 40, 30}
# 從 a 裡面移除 40
a.remove(40)               # {1, 3, 100, 5, 6, 30}


x = [1,3,5,6,30,40]
# 把 100 加入 x 裡面
#????

# 從 x 裡面移除 40
#????






# 如果有很多要加進去
#x = [10,20,30,30,50]
# 把 x(集合/清單/迭代物件) 加入 a 裡面
#a.update(x)


# x = [1,2,3,3,5,6,6,6,6,5,1]
# y = [10,20,30,40]

# z = x+y
# print(z)  # [1, 2, 3, 3, 5, 6, 6, 6, 6, 5, 1, 10, 20, 30, 40]

# a = set([1,3,5,6,30,40])
# b = set([10,20,30,40])

# #c = a+b                      # set不能相加
# #c = set(list(a) + list(b))   #繞道 轉回清單處理
# #c = a.union(b)               # union  聯集
# c = a | b                     # |
# print(c)



# x = [1,2,3,3,5,6,6,6,6,5,1]

# a = set(x)

# print(x)   #[1, 2, 3, 3, 5, 6, 6, 6, 6, 5, 1]
# print(a)   #{1, 2, 3, 5, 6}

# #b = {1, 2, 3, 5, 6}   #????
# #print(b)

# y = list(a)
# print(y)   #[1, 2, 3, 5, 6]

# # 去掉x中重複的部分 (第二次出現)
# x = list(set(x))