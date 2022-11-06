from tkinter import *
Num = 0
root = Tk()
root.title("Class4_HW1")
root.geometry("400x400+150+200")
mylabel = Label(root, text="點擊按鈕次數", fg="orange", font=("Courier",18,"bold"))
mylabel.pack()
Num += 1
def clicked():
    Label1 = Label(root, text= Num)
    Label1.pack()
mybuttom = Button(root, text="Click Me", command=clicked)
mybuttom.pack()
root.mainloop()