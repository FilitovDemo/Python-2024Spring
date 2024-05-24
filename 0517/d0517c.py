# x = input('請輸入密碼')
# while x!='apple':
#     print('密碼錯誤')
#     x = input('請重新輸入密碼')

# while True:
#     x = input('請輸入密碼')
#     if x=='apple':
#         break
#     print('密碼錯誤')

def password():
    x = input('請輸入密碼')
    while x!='apple':
        print('密碼錯誤')
        x = input('請重新輸入密碼')


def password2():
    while True:
        x = input('請輸入密碼')
        if x=='apple':
            return
        print('密碼錯誤') 


def passwordlimit():
    for _ in range(3):
        x = input('請輸入密碼')
        if x=='apple':
            return
        print('密碼錯誤') 
    print('密碼錯誤三次,離開程式....')
    exit()            #直接離開程式


passwordlimit()
print('密碼正確,繼續往下執行..')
#其他的程式碼