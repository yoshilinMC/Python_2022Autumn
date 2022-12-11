from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("HW1")
root.geometry("400x400+150+200")

def clicked_plus():
    Label_Num["text"] = int(Label_Num["text"])+1
def clicked_minus():
    if int(Label_Num["text"])>0:
        Label_Num["text"] = int(Label_Num["text"])-1

def ClickRadiobtn1():
    Label_Choose["fg"] = "Black"
    Label_Choose["textvariable"] = val
def ClickRadiobtn2():
    Label_Choose["fg"] = ""
    Label_Choose["textvariable"] = val
def ClickRadiobtn3():
    Label_Choose["fg"] = "Brown"
    Label_Choose["textvariable"] = val

Img = Image.open("C:/Users/yoshi_pgnry07/Downloads/sofa.jpg")
resized_image = Img.resize((100,100))
tk_img = ImageTk.PhotoImage(resized_image)

Label_Title = Label(root, text="Kube shop")
Label_Pic = Label(root, image=tk_img)
Label_Sell = Label(root, text="沙發組")
Button_Plus = Button(root, text="+", command=clicked_plus)
Label_Num = Label(root, text="0")
Button_Minus = Button(root, text="-", command=clicked_minus)
Label_Money = Label(root, text="$ 1200")

Label_Title.grid(row=1,column=0, sticky=E)
Label_Pic.grid(row=2,column=0, sticky=W)
Label_Sell.grid(row=3,column=0, sticky=W)
Label_Money.grid(row=3,column=1, sticky=W)
Button_Minus.grid(row=4, column=1, sticky=W)
Label_Num.grid(row=4,column=1)
Button_Plus.grid(row=4,column=1, sticky=E)

val = StringVar()
Radiobtn1 = Radiobutton(root, text="balck", variable=val, value="black", fg="black", command=ClickRadiobtn1)
Radiobtn1.grid(row=1,column=1, sticky=E)
Radiobtn2 = Radiobutton(root, text="gray", variable=val, value="gray", fg="gray", command=ClickRadiobtn2, state="disabled")
Radiobtn2.grid(row=2,column=1)
Radiobtn3 = Radiobutton(root, text="brown", variable=val, value="brown", fg="brown", command=ClickRadiobtn3)
Radiobtn3.grid(row=2,column=1, sticky=S)
Label_Choose = Label(root, textvariable=val)
Label_Choose.grid(row=3, column=0, sticky=E)

root.mainloop()