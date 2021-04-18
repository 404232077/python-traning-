#集合的運算
# s1={1,2,3}
# print(3 in s1)
# print(3 not in s1)

# s1={1,3,5}
# s2={3,5,7}
# s3=s1&s2    #&交集:取兩個集合，中相同的資料
# print(s3)

# s1={1,3,5}
# s2={5,7,9}
# s3=s1|s2    #|連集:取兩個集合中的所有資料，但不重複
# print(s3)

# s1={111,7,55}
# s2={5,7,9,11}
# s3=s1-s2    #差集:從s1中減去s2中重複的部分
# print(s3)
# s4=s2-s1
# print(s4)
# s5=s1^s2    #反交集:取兩個集合中，不重複的部分
# print(s5)

# s=set("Hello")  #set(字串):拆解成集合
# print(s)

#字典的運算: key-value 配對
# d={"apple":"蘋果","bug":"蟲蟲"}
# d["apple"]="小蘋果"
# print(d["apple"])
# print("apple" in d)
# del d["bug"]    #刪除字典中鍵值對
# print(d)

# dic={x:x+3 for x in [1,3,5]}    #從列表的資料當基礎產生字典
# print(dic)

#ch9_3
# fruit = {"香蕉":50,"蘋果":100,"鳳梨":500}   #冒號前是鍵，冒號後是值
# print("鳳梨一斤",fruit["鳳梨"],"元")

# ch9_4 增加字典內容
# fruit = {"香蕉":50,"蘋果":100,"鳳梨":500}   
# fruit["西瓜"] = 800
# print("西瓜一斤",fruit["西瓜"],"元")

#ch9_27 明星賽投票
# vote_dict = {}
# vote_survey = True
# while vote_survey:
#     name = input("請輸入你的名字: ")
#     player = input("請輸入你要投票給哪位球員: ")
#     vote_dict[name] = player
#     c = input("是否繼續投票(y/n): ")
#     if c != "y":
#         vote_survey = False
# else:
#     print(vote_dict)


