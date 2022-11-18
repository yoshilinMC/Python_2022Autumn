from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("class6")

# 設定視窗座標位置
root.geometry("300x300")

mylabel = Label(root, text="kube shop").grid(row=0,column=1, sticky=E)
mylabel2 = Label(root, text="戶外餐桌椅組").grid(row=1,column=0)
mylabel3 = Label(root, text="$1200").grid(row=2,column=0, sticky=W)
MyButton = Button(root, text="+").grid(row=3,column=0, sticky=W)
mylabel4 = Label(root, text="0").grid(row=3,column=1, sticky=W)
MyButton2 = Button(root, text="-").grid(row=3,column=2, sticky=E)

root.mainloop()