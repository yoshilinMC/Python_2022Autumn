# 引入 tkinker module
from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("TITLE")

# 設定視窗座標位置
root.geometry("300x300+500+300")

# 建立 Label 標籤
mylabel = Label(root, text="Enter Your Name", fg="lightskyblue", bg="black", font=("Pilgi",20,"italic"))
# 加入視窗中
mylabel.pack(pady=20)

# 建立 Input Entry Boxes
e = Entry(root)
# 加入視窗中
e.pack()

# 點擊按鈕函式 function
def clicked():
    Label1 = Label(root, text= e.get())
    Label1.pack()
# 建立 buttom 按鈕
mybuttom = Button(root, text="Enter!", command=clicked)
# 加入視窗中
mybuttom.pack(pady=20)

# 執行主程式
root.mainloop()