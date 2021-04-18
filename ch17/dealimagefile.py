# from PIL import Image
# chu = Image.open("CHU.jfif")
# chu.show()


# from PIL import Image
# crayon = Image.open("crayon.jfif")
# print(type(crayon))
# width, height = crayon.size
# print("寬度: %d\n高度: %d"%(width, height))

#轉換副檔名
# from PIL import Image
# crayon = Image.open("crayon.jfif")
# crayon.save("crayon.png")

#建立新的影像物件
# from PIL import Image
# pict1 = Image.new("RGBA",(300,180),"aqua")
# pict1.show()
# pict1.save("pict.png")

#裁切影像
# from PIL import Image
# pict = Image.open("crayon.png")
# print(pict.size)

# croppict1 = pict.crop((50,5,160,100))
# croppict1.show()
# croppict1.save("crayon1.png")

# croppict2 = pict.crop((160,70,250,174))
# croppict2.show()
# croppict2.save("crayon2.png")

# 將裁切圖片填滿影像區間
# code practice 1
# from PIL import Image
# pict = Image.open("crayon.png")
# pict1 = Image.open("crayon1.png")
# pict.paste(pict1,(0,0))
# pict.paste(pict1,(110,0))
# pict.show()

# code practice 2
# from PIL import Image
# pict = Image.new("RGBA",(1100,475),"aqua")
# pict1 = Image.open("crayon1.png")
# pict2 = Image.open("crayon2.png")
# for x in range(0,1100,220):
#     for y in range(0,475,95):
#         pict.paste(pict1,(x,y))

# for x in range(110,1100,220):
#     for y in range(0,475,95):
#         pict.paste(pict2,(x,y))

# pict.show()

# 文字辨識
# from PIL import Image
# import pytesseract

# text = pytesseract.image_to_string(Image.open("ABC.png"))
# print(text)

#車牌辨識系統
# from PIL import Image
# import time
# import pytesseract

# cardict = {}
# parking = True
# while parking:
#     carpict = input("車牌圖檔: ")
#     carnum = pytesseract.image_to_string(Image.open(carpict))
#     if carpict == "q":
#         break
#     elif carnum in cardict:
#         outtime = time.asctime()
#         print("謝謝光臨\n車牌: %s\n出場時間: %s"%(carnum,outtime))
#     else:
#         intime = time.asctime()
#         cardict[carnum] = intime
#         print("歡迎停車\n車牌: %s\n進場時間: %s"%(carnum,intime))
