#有序可變動列表 List
# grades=[12,60,15,70,90]
# grades[1:4]=[]   #連續刪除列表中編號1到4(不包刮)的資料
# print(grades)

# grades[0]=88
# print(grades)

# grades+=[56,72]
# print(grades)

# grades=[12,60,15,70,90]
# length=len(grades)
# print(length)

#巢狀列表
# data=[[5,7,2],[6,8,1]]
# data[0][0:4]=[6,6,6,6]
# data[1][0]=9
#print(data)

#有序不可變動列表 tuple
# data=(5,6,7)
# data[2]=8   #錯誤，tuple不可變動
# print(data[2])

#ch8_16 zip()
# player = ["Parker","Duncan","Ginobilly"]
# score = [25,27,19]
# zipdata = zip(player,score)
# print(type(zipdata))
# games = tuple(zipdata)
# print(games)
# output: 
# <class 'zip'>
# (('Parker', 25), ('Duncan', 27), ('Ginobilly', 19))