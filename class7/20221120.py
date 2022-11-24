# from tkinter import *

# root = Tk()
# root.title("class6")
# root.geometry("350x100")

# Frame元件
# frame1 = Frame(root, pady=5, padx=20, bg="lightblue")
# frame2 = Frame(root, pady=20, padx=10, bg="pink")

# # 將 Frame 裡的 Label
# Label1 = Label(frame1, text="Hello", width=10)
# Label1.pack()
# Label2 = Label(frame2, text="World", width=20)
# Label2.pack()

# frame2.pack()
# frame1.pack()


# frame1 = Frame(root, pady=10, padx=10, bg="lightgreen")
# frame2 = Frame(root, pady=10, padx=10, bg="lightblue")

# Label1 = Label(frame1, text="Hello", width=10)
# Label1.pack()
# Label2 = Label(frame2, text="World", width=10)
# Label2.pack()

# frame1.pack(side="left")
# frame2.pack(side="right")


from tkinter import *
Num = 0
root = Tk()
root.title("Class7")
root.geometry("400x400+150+200")
counter = 0

# 方法一
def clicked():
    global counter
    counter += 1
    mylabel["text"] = "clicked" + str(counter)

# 方法二
# def clicked():
#     global counter
#     counter += 1
#     mystringvar.set("click" + str(counter))
# mystringvar = StringVar()
# mystringvar.set("click 0")

mybuttom = Button(root, text="Buttom", command=clicked)
mybuttom.pack()
mylabel = Label(root, text="0")
mylabel.pack()

# 獲取 label 文字內容
# 方法一
# mylabel = Label(root, text="Hello World")
# mylabel.pack()
# Label(root, text=mylabel["text"]).pack()
# 方法二
# mystringvar = StringVar()
# mystringvar.set("Hello World")
# mylabel = Label(root, textvariable=mystringvar)
# mylabel.pack()
# Label(root, text=mystringvar.get()).pack()

# mystringvar = StringVar()
# mystringvar.set("Hello World!")
# mylabel = Label(root, textvariable=mystringvar).pack()
# mybuttom = Button(root, text="Get label text").pack()
# Label(root, text=mystringvar.get()).pack()
# Label(root, text=mystringvar.get()).pack()
# Label(root, text=mystringvar.get()).pack()

root.mainloop()