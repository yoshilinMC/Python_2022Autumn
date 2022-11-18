from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("class6")

# 設定視窗座標位置
root.geometry("300x300")
"""
# anchor = 元件在容器的位置 : E,W,S,N,Center(預設),NE,SE,SW,NW
MyButton1 = Button(root, text="東").pack(anchor = E)
MyButton2 = Button(root, text="西").pack(anchor = W)
MyButton3 = Button(root, text="南").pack(anchor = S)
MyButton4 = Button(root, text="北").pack(anchor = N)
MyButton5 = Button(root, text="東南").pack(anchor = SE)
MyButton6 = Button(root, text="西北").pack(anchor = NW)
"""
"""
MyButton1 = Button(root, text="MyButton1").grid(row=0,column=0)
MyButton2 = Button(root, text="MyButton2").grid(row=0,column=1)
MyButton3 = Button(root, text="MyButton3").grid(row=0,column=2)
MyButton4 = Button(root, text="MyButton4").grid(row=1,column=0)
MyButton5 = Button(root, text="MyButton5").grid(row=1,column=2)
MyButton6 = Button(root, text="MyButton6").grid(row=2,column=1)
"""
"""
# rowspan(columnspan) = 處存格合併列(行)數
MyButton1 = Button(root, text="MyButton1").grid(row=0,column=0)
MyButton2 = Button(root, text="MyButton2").grid(row=0,column=1)
MyButton3 = Button(root, text="MyButton3").grid(row=0,column=2)
MyButton4 = Button(root, text="MyButton4").grid(row=1,column=0, columnspan=2)
MyButton5 = Button(root, text="MyButton5").grid(row=1,column=2)
"""
"""
# sticky = 元件於網格中的位置 : E,W,S,N,Center(預設)
MyButton1 = Button(root, text="MyButton1").grid(row=0,column=0)
MyButton2 = Button(root, text="MyButton2").grid(row=0,column=1)
MyButton3 = Button(root, text="MyButton3").grid(row=0,column=2)
MyButton4 = Button(root, text="MyButton4").grid(row=1,column=0, columnspan=2, sticky=W+E)
MyButton5 = Button(root, text="MyButton5").grid(row=1,column=2)
"""
"""
mylabel1 = Label(root, text="Width").grid(row=0,column=0)
mylabel2 = Label(root, text="Height").grid(row=1,column=0)
enterbox = Entry(root).grid(row=0,column=1)
enterbox = Entry(root).grid(row=1,column=1)
buttom = Button(root, text="Result").grid(row=0,column=2,rowspan=2, sticky=N+S)
# """
# """
# 建立主選單
menu = Menu(root)
# 建立子選單，選單綁定 menubar 主選單(tearoff=0)
menubar1 = Menu(menu, tearoff=0)
# 子選單項目
menubar1.add_command(label="Open")
menubar1.add_command(label="Save")
menubar1.add_command(label="Exit")
# 建立主選單，內容為子選單
menu.add_cascade(label="File",menu=menubar1)
# 建立第二個選單的子選單，有三個選項
menubar2 = Menu(menu, tearoff=0)
menubar2.add_command(label="AAA")
menubar2.add_command(label="BBB")
menubar2.add_command(label="CCC")

# 子選單分隔線
menubar2.add_separator()
# 建立選單內的子選單，有三個選項
menubar2more = Menu(menubar2, tearoff=0)
menubar2more.add_command(label="x")
menubar2more.add_command(label="y")
menubar2more.add_command(label="z")
menubar2.add_cascade(label="File", menu=menubar2more)
# 建立第二個選項 File ，綁定子選單
menu.add_cascade(label="Test", menu=menubar2)
# 主視窗加入主選單
root.config(menu=menu)
# """

# def open(): print("open")
# def save(): print("save")
# def exit():
#     print("exit")
#     root.destroy()

# menu = Menu(root)
# menubar = Menu(menu, tearoff=0)
# menubar.add_command(label="Open", command=open)
# menubar.add_command(label="Save", command=save)
# menubar.add_command(label="Exit", command=exit)
# menu.add_cascade(label="File",menu=menubar)
# root.config(menu=menu)

# 執行主程式
root.mainloop()