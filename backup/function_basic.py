# def multip(n1,n2):    # 定義函式，函式內部的程式碼，若沒有呼叫，就不會執行
#     print(n1*n2)
# multip(3,5)   #呼叫函式
# multip(20,20)

# def calculate(n):
#     sum = 0
#     for x in range(1,n+1):
#         sum += x
#     print(sum)
#     return(sum)
# x = int(input("請輸入一個數字: "))
# calculate(x)

# 無限/不定參數資料
# def average(*numbers):
#     sum = 0
#     for x in numbers:
#         sum += x
#     print(sum/len(numbers))
#     return(sum/len(numbers))
# average(1,2,3,4)
# average(1,2,3,)
# output:
# 2.5
# 2.0

# ch11_13 return 多筆資料
# def math(x,y):
#     add = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     return(add,sub,mul,div)

# lists = [adds,subs,muls,divs] = math(2,5)
# print(lists)

# ch11_19
# def seminar(name):
#     str1 = "親愛的: "
#     str2 = "公司預計在下周三舉行研討會，歡迎出席。"
#     str3 = "經理: 朱大帥"
#     for member in name:
#         print(str1,member)
#         print(str2)
#         print(str3)
#         print("")
#     return()
# names = ["Parker","Aana","Cindy"]
# seminar(names)
