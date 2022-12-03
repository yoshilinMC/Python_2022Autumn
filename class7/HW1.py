from tkinter import *
root = Tk()
root.title("Class7")
root.geometry("400x400+150+200")

def clicked_plus():
    mylabel4["text"] = int(mylabel4["text"])+1
    mylabel5["text"] = "總額 : $" + str(int(mylabel4["text"])*1200) + "元"
def clicked_minus():
    if int(mylabel4["text"])>0:
        mylabel4["text"] = int(mylabel4["text"])-1
        mylabel5["text"] = "總額 : $" + str(int(mylabel4["text"])*1200) + "元"

mylabel = Label(root, text="kube shop")
mylabel2 = Label(root, text="戶外餐桌椅組")
mylabel3 = Label(root, text="$1200")
MyButton = Button(root, text="+", command=clicked_plus)
mylabel4 = Label(root, text="0")
MyButton2 = Button(root, text="-", command=clicked_minus)
mylabel5 = Label(root, text="總額 : $0元")

mylabel.grid(row=0,column=1,columnspan=4, sticky=W+E+N+S)
mylabel2.grid(row=1,column=0, columnspan=2, sticky=W)
mylabel3.grid(row=1,column=2, sticky=W)
MyButton.grid(row=3,column=2, sticky=W)
mylabel4.grid(row=3,column=2)
MyButton2.grid(row=3,column=2, sticky=E)
mylabel5.grid(row=4,column=2, sticky=W)

root.mainloop()