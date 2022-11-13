from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("")

# 設定視窗座標位置
root.geometry("500x500")

MyButton1 = Button(root, text="button1")
MyButton1.pack()
MyButton2 = Button(root, text="button2")
MyButton2.pack(side="left")
MyButton3 = Button(root, text="button3")
MyButton3.pack(side="bottom")

# 執行主程式
root.mainloop()