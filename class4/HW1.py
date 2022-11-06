from tkinter import *
Num = 0
# 建立主視窗
root = Tk()
# 設定視窗標題
root.title("Class4_HW1")
# 設定視窗大小為
root.geometry("400x400+150+200")
mylabel = Label(root, text="點擊按鈕次數", fg="orange", font=("Courier",25,"bold"))
mylabel.pack()
# 計算點擊次數
def clicked():
    global Num
    Num += 1
    Label1 = Label(root, text= Num)
    Label1.pack()
# 設定按鈕
mybuttom = Button(root, text="Click Me", command=clicked)
mybuttom.pack()
root.mainloop()