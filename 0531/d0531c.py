a = [10,20,30,40]

#-------------------------------
# 過濾  逐個檢驗
# filter(判斷函數,清單)
# 清單 --> 逐個->函數->通過與否 --> 清單(filter物件)

def isBigger(x):
    if x>=30:
        return True     #要留下來的 回傳True
    return False        #要捨棄的 回傳False

p = list(filter(isBigger,a))

print(p)

################
#等價
# p = []
# for x in a:
#     if isBigger(x):
#         p.append(x)