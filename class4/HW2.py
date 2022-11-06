from tkinter import *
root = Tk()
root.title("Class4_HW2")
root.geometry("300x300+500+300")
mylabel = Label(root, text="Enter Your Birth Date", font=("Arial"))
mylabel.pack()
mylabel2 = Label(root, text="Input format is yyyy.mm.dd", font=("Arial"))
mylabel2.pack()
e = Entry(root)
e.pack()
def clicked():
    y = e.get()[0:4]
    Num = int(y)
    Num = 2022 - int(y)
    Label1 = Label(root, text= Num)
    Label1.pack()
mybuttom = Button(root, text="Enter!", command=clicked)
mybuttom.pack()
root.mainloop()