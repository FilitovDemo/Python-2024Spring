#類型2 具名的索引

scores = {
    'alice': 60,
    'bob': 80,
    'cathy': 75,
    'debbie': 66,
    'eva': 90,
    'flora': 50
}

# 找到 cathy 的成績
print( scores['cathy'] )

#班上同學的成績
names = ['alice','bob','cathy','debbie','eva','flora']
scores = [60,80,75,66,90,50]

# # 找到 cathy 的成績
# # 在 names 找到 cathy 的位置??
# # i = 0
# # while i<len(names):
# #     if names[i]=='cathy':
# #         break
# #     i = i+1
# i = names.index('cathy')
# # 在 scores[位置] 取得他的成績
# print( scores[i] )

# print( scores[names.index('cathy')] )