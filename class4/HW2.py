from tkinter import *
from datetime import *
# 建立主視窗
root = Tk()
# 設定視窗標題
root.title("Class4_HW2")
# 設定視窗大小為
root.geometry("300x300+500+300")
mylabe = Label(root, text="Enter Your Birth Date:\nInput format is yyyy.mm.dd", font=("Arial"))
mylabe.pack()
enterbox = Entry(root,width=30, font = ("Arial",18,"bold"))
enterbox.pack()
def clicked():
    T_S = enterbox.get()
    T1 = datetime.strptime(T_S, "%Y.%m.%d")
    T2 = datetime.now()
    result = T2.year-T1.year
    label = Label(root, text= "You are "+str(result)+" years old")
    label.pack()
# 設定按鈕
mybuttom = Button(root, text="Enter!", command=clicked, font = ("Garamond", 16))
mybuttom.pack(pady = 20)
root.mainloop()