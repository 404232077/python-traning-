# while 迴圈 1+2+...+10
#n=1
#sum=0
#while n<=10 :
#    sum=sum+n
#    n+=1
#print(sum)

# for 迴圈
#for x in [1,3,5]:
#    print(x)

#for x in "Hello":
#    print(x)

#for x in range(4):
#    print(x)

# for 1+2+...+10
# sum=0
# for x in range(1,11):
#     sum=sum+x
# print(sum)

# ch7_3
# players = ["Duncan","Parker","Ginobilly","Curry","Harden"]
# for player in players:
#     print(player,end=", ")

# ch7_6
# players = ["duncan","parker","ginobilly","curry","harden","westbrook","diaw","labron","bosh","allen","fox"]
# print("明星賽得票率前三高球員: ")
# for f3 in players[:3]: print(f3.title(),end=", ")
# print("")
# print("明星賽得票率前三低球員: ")
# for l3 in players[-3:]: print(l3.title(),end=", ")
# print("")

# ch7_7
# files = ["chu.py","pig.c","games.py","web.css","mouse.py","lab.html"]
# py= []
# for file in files:
#     if file.endswith(".py"):    #endswith 用法
#         py.append(file)
# print(py)

# ch7_8
# lists = ["朱大帥","朱老六","王老七","張老八","朱老九"]
# samelastname = []
# for i in lists:
#     if i.startswith("朱"):    #starswith 用法
#         samelastname.append(i)
# print(samelastname)

#ch7_9
# fruit1 = ["apple","pineapple","banana","orange","watermelon"]
# fruit2 = ["apple","orange"]
# for i in fruit1:
#     if i in fruit2: fruit1.remove(i)
# print(fruit1)

#ch7_11
# money = int(input("請輸入你的存款: "))
# rate = float(input("請輸入銀行利率: "))
# years = int(input("請輸入年數: "))
# interest = 0
# for i in range(0,years+1):
#     money *= (1+rate)
# print(money)

#ch7_13
# sum = 0
# for i in range(11):
#     sum += i
# print(sum)

#ch7_14
# squares = []
# square = 0
# i = int(input("輸入: "))
# for x in range(i+1):
#     square = x**2
#     squares.append(square)
# print(squares)

#ch7_14 進階
# num = int(input("輸入: "))
# square = [num**2 for num in range(num+1)]
# print(square)

#ch7_15
# x = []
# for i in range(6):
#     x.append(i)
# print(x)

#ch7_15 進階
# x = [list(range(6))]
# print(x)

#ch7_15 再進階
# x = [i for i in range(6)]
# print(x)

#ch7_17
# C = [15,20,25]
# F = [C*9/5+32 for C in list(C)]
# print(F)

#ch7_25
# scores = [20,22,18,32,10,81,52,63]
# scores.sort(reverse = True)
# f3 = []
# count = 0
# for KB in scores:
#     f3.append(KB)
#     count += 1
#     if count == 3:
#         break
# print(f3)
#output: [81, 63, 52]

#ch7_26
# scores = [22,38,29,33,63,18,39]
# games = 0
# for TD in scores:
#     if TD >= 30:
#         games += 1
# print("%d"%games)
# output:　４

#ch7_30
# msg = "我是鸚鵡，你想說甚麼:"
# msg1 = ""
# while msg1 != "q":
#     msg1 = input(msg)
#     if msg1 != "q":
#         print(msg1)
# else:
#     print("您已結束對話")

#ch7_32
# guess = int(input("請輸入一個數字: "))
# num = int(input("猜: "))
# while num != guess:
#     if num >= guess:
#         print("小一點")
#     elif num <= guess:
#         print("大一點")
#     num = int(input("猜: "))
# else:
#     print("猜對了")

#ch7_35
# for x in range(1,10):
#     for y in range(1,10):
#         print("%d*%d=%d"%(x,y,x*y),end = ",")
#     print("")

# x = 0
# y = 0
# while x <= 9:
#     x += 1
#     while y <= 9:
#         y += 1
#         print("%d*%d=%d"%(x,y,x*y),end = ",")
#     else:
#         y = 0
#         print("")

#ch7_42
# players = ["Parker","Duncan","Ginobilly"]
# for x in enumerate(players):
#     print(x)

# for x in enumerate(players,10):
#     print(x)

#ch7_43
# scores = [52,38,58,20,28,16,20,17]
# count = 0
# print("低於20分的場次分別為: ")
# for x in scores:
#     count += 1
#     if x <= 20:
#         print("第%d場%d分"%(count,x))
# 低於20分的場次分別為:
# 第4場20分
# 第6場16分
# 第7場20分
# 第8場17分

# scores = [52,38,58,20,28,16,20,17]
# print("低於20分的場次分別為: ")
# for count,score in enumerate(scores,1):   #enumerate 用法
#     if score <= 20:
#         print("第%d場%d分"%(count,score))
# 低於20分的場次分別為:
# 第4場20分
# 第6場16分
# 第7場20分
# 第8場17分

#ch7_43
# msg = "歡迎來到豬大帥商店，店內商品有:"
# msg1 = ["鍋子","牙刷","牙膏","冰箱","保險套","電視","電腦","水壺","面膜","飲水機"]
# msg2 = ""
# msg3 = []
# while True:
#     msg2 = input("請輸入你要買的東西: ")
#     if msg2 in msg1:
#         msg3.append(msg2)
#     elif msg2 == "Q" or msg2 == "q":
#         print("你買的物品為:",msg3)
#         break
#     else:
#         print("沒賣")
