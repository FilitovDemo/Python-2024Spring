x = [3,2,4,2,1,5,8,5,7,6,9,7,5,2]

#c = [0]*10
c = [0,0,0,0,0,0,0,0,0,0]
#   c[0]放 0 出現的次數
#   c[1]放 1 出現的次數
#   c[2]放 2 出現的次數

for a in x:  #處理x中的每一個數字
    c[a] = c[a]+1  #計算a出現的次數


# print('0出現',c[0],'次')
# print('1出現',c[1],'次')
# print('2出現',c[2],'次')

i = 0
for n in c:
    print(i,' ',n,'次 ','X'*n)
    i = i+1

# i = 0
# while i<len(c):
#     print(i,'出現',c[i],'次')
#     i = i+1

# for i,n in enumerate(c):
#     print(i,'出現',n,'次')

