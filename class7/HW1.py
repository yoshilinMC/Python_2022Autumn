from tkinter import *
root = Tk()
root.title("Class7")
root.geometry("400x400+150+200")
counter = 0
Num = 0

def clicked_plus():
    global counter
    global Num
    counter += 1
    Num += 1200
    mylabel4["text"] = str(counter)
    mylabel5["text"] = "總額 : $" + str(Num) + "元"
def clicked_minus():
    global counter
    global Num
    if counter != 0:
        counter -= 1
        Num -= 1200
    mylabel4["text"] = "總額 : $" + str(Num) + "元"


mylabel = Label(root, text="kube shop").grid(row=0,column=1,columnspan=4, sticky=W+E+N+S)
mylabel2 = Label(root, text="戶外餐桌椅組").grid(row=1,column=0, columnspan=2, sticky=W)
mylabel3 = Label(root, text="$1200").grid(row=1,column=2, sticky=W)
MyButton = Button(root, text="+", command=clicked_plus).grid(row=3,column=2, sticky=W)
mylabel4 = Label(root, text="0").grid(row=3,column=2)
MyButton2 = Button(root, text="-", command=clicked_minus).grid(row=3,column=2, sticky=E)
mylabel5 = Label(root, text="總額 : $0元").grid(row=4,column=2, sticky=W)

root.mainloop()