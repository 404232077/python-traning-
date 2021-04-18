#1 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# n=int()
# for n in range (1500,2701):
#     if (n%7==0) and (n%5==0):
#         print(n)

#2 Write a Python program to convert temperatures to and from celsius, fahrenheit.
# idegree = int(input("請輸入溫度: "))
# odegree = int()
# iconvention = input("清輸入溫度符號(c or f): ")

# if iconvention == "c":
#     odegree = (9*idegree+(32*5))/5
#     oconvention = "Fahrenheit"
# elif iconvention == "f":
#     odegree = (9*idegree+(32*5))/5
#     oconvention = "Celsius"
# else:
#     print("符號輸入錯誤")
#     quit()

# print(odegree, oconvention)

#3 Write a Python program to guess a number between 1 to 9.
# import random
# r = random.randint(0,10)
# number = int(input("請輸入一個1到9的數字: "))
# while number in range(0,10):
#     if number == r:
#         print("you are so fucking good")
#         break
#     else:
#         print("wrong guess")
#         number = int(input("請輸入一個1到9的數字: "))
# else:
#     print("wrong number")

#4 Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n=5
# for i in range(n):
#     for j in range(i):
#         print("* ",end="")
#     print(" ")

# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("* ",end="")
#     print(" ")

# n=0
# sum=1
# while n <= 4:
#     n += 1
#     sum=1
#     while sum <= n:
#         sum += 1
#         print("* ",end="")
#     print(" ")

# n=5
# while n >= 1:
#     n -= 1
#     sum=1
#     while sum <= n:
#         sum += 1
#         print("* ",end="")
#     print(" ")
# print(" ")

#成績分類問題
# score = int(input("請輸入成績: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("不及格")
