from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Class8")
root.geometry("400x400+150+200")
counter = 0

## 更改Buttom文字內容
# 1
# def clicked():
#     global counter
#     counter += 1
#     mybuttom["text"] = "clicked" + str(counter)
# 2
# def clicked():
#     global counter
#     counter += 1
#     mystringvar.set("click" + str(counter))
# mystringvar = StringVar()
# mystringvar.set("click 0")
# mybuttom = Button(root, textvariable=mystringvar, command=clicked)
# mybuttom.pack()

## 獲取Buttom文字內容
# 方法一
# MyButton = Button(root, text="Hello World")
# MyButton.pack()
# Label(root, text=MyButton["text"]).pack()
# 方法二
# mystringvar = StringVar()
# mystringvar.set("Hello World")
# MyButton = Button(root, textvariable=mystringvar)
# MyButton.pack()
# Label(root, text=mystringvar.get()).pack()

# 開啟圖片
# Img = Image.open("/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class8/corgi1.jpg")
# 轉換為 TK 圖片物件
# TK_Img = ImageTk.PhotoImage(Img)
# 在 Label 中放入圖片
# label = Label(root, image=TK_Img)
# label.pack()
# 在 Button 中放入圖片
# MyButton = Button(root, image=TK_Img)
# MyButton.pack()

# 開啟圖片
# Img = Image.open("/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class8/corgi1.jpg")
# 更改圖片大小
# resized_image = Img.resize((100,100))
# 轉換成 TK 圖片物件
# tk_img = ImageTk.PhotoImage(resized_image)
# label = Label(root, image=tk_img)
# label.pack()

#　引入 messagebox
from tkinter import messagebox
# 出現"message test"的普通訊息框
messagebox.showinfo("showinfo", "message test")
# 出現提問訊息框
# result = messagebox.askquestion("askquestion", "is it sunday?")
# print("user clicked "+result)

root.mainloop() 