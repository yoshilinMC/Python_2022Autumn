from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("")

# 設定視窗座標位置
root.geometry("500x500")

"""
# side = Top(預設), Bottom, Left, Right
# 建立 Label 標籤
MyButton1 = Button(root, text="West")
MyButton2 = Button(root, text="East")
MyButton3 = Button(root, text="East2")
# 加入視窗中
MyButton1.pack(side="left")
MyButton2.pack(side="right")
MyButton3.pack(side="right")

# fill = 填滿所分配空間之方向:None(預設),X,Y,Both
# 加入視窗中
MyButton1.pack(fill="x")
MyButton2.pack(side="right", fill="y")

# expend = 填滿容器:True/False(預設)
MyButton1 = Button(root, text="expand=0")
MyButton1.pack(fill="both", expand=0)
MyButton2 = Button(root, text="expand=1")
MyButton2.pack(fill="both", expand=1)
"""
# padx(y) = 元件邊框與容器之距離(px, 預設=0)
# MyButton1 = Button(root, text="West")
# MyButton1.pack(side="left", padx=20)
# MyButton2 = Button(root, text="East")
# MyButton2.pack(side="right", padx=30)
# ipadx(y) = 元件內容(文字/圖像)與其邊框之距離(px, 預設=0)
# MyButton1.pack(side="left", ipadx=30)
# MyButton2.pack(side="right", ipady=30)

# MyButton1 = Button(root, text="button1")
# MyButton1.pack()
# MyButton2 = Button(root, text="button2")
# MyButton2.pack(side="left")
# MyButton3 = Button(root, text="button3")
# MyButton3.pack(side="bottom")

MyButton1 = Button(root, text="button1")
MyButton1.pack(fill="x", pady=10)
MyButton2 = Button(root, text="button2")
MyButton2.pack(side="left",fill = "y")
MyButton3 = Button(root, text="button3")
MyButton3.pack(side="left", padx=20)
MyButton4 = Button(root, text="button4")
MyButton4.pack(side="right", padx=20)
MyButton5 = Button(root, text="button5")
MyButton5.pack(pady=10)

# 執行主程式
root.mainloop()