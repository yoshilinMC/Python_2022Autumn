from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Class7")
root.geometry("300x200")

def clicked_plus():
    Label_Num["text"] = int(Label_Num["text"])+1
def clicked_minus():
    Label_Num["text"] = int(Label_Num["text"])-1

# # 開啟圖片
Img = Image.open("C:/Users/yoshi_pgnry07/Downloads/sofa.jpg")
# 更改圖片大小
resized_image = Img.resize((100,100))
# 轉換成 TK 圖片物件
tk_img = ImageTk.PhotoImage(resized_image)

Label_Title = Label(root, text="Kube shop")
Label_Pic = Label(root, image=tk_img)
Label_Sell = Label(root, text="沙發組")
Button_Plus = Button(root, text="+", command=clicked_plus)
Label_Num = Label(root, text="0")
Button_Minus = Button(root, text="-", command=clicked_minus)
Label_Money = Label(root, text="$ 1200")

Label_Title.grid(row=1,column=0, sticky=E)
Label_Pic.grid(row=2,column=0, sticky=W)
Label_Sell.grid(row=3,column=0, sticky=W)
Label_Money.grid(row=3,column=1, sticky=W)
Button_Minus.grid(row=4, column=1, sticky=W)
Label_Num.grid(row=4,column=1)
Button_Plus.grid(row=4,column=1, sticky=E)

root.mainloop() 