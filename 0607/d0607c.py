#filter 過濾
#filter(檢核函數,清單)
#         True/False
a = [3,5,7,9,4,8,6,2,1]

#b = [a清單中的奇數]

#方法1
b = []
for x in a:
    if x%2==1:
        b.append(x)

#方法2
b = [x for x in a if x%2==1]

#方法3
def exam(x):
    if x%2==1:
        return True
    return False

b = list(filter(exam,a))

#方法3 lambda縮短
b = list(filter(lambda x:True if x%2==1 else False, a))
