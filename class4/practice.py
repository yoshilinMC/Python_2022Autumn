from tkinter import *
root = Tk()
root.title("class4")
root.geometry("600x400+150+200")

# mylabel = Label(root, text="10/2", fg="blue", bg="purple", font=("Arial",16,"bold"))
# mylabel.pack()
# mylabe2 = Label(root, text="Sunday", fg="blue", bg="purple", font=("Pilgi",20,"italic"))
# mylabe2.pack(pady=50)

mylabel = Label(root, text="Enter ur name", fg="blue", font=("Impact",20,"bold"))
mylabel.pack()

e = Entry(root)
e.pack()

def clicked():
    Label1 = Label(root, text= e.get())
    Label1.pack()
mybuttom = Button(root, text="Enter!", command=clicked)
mybuttom.pack(pady=20)



root.mainloop()