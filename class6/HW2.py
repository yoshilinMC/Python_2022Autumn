from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("class6")

# 設定視窗座標位置
root.geometry("300x300")

def Open(): Execute="normal"
def Execute(): pass
def Close(): Execute="disable"

menu = Menu(root)
menubar2 = Menu(menu, tearoff=0)
menubar2.add_command(label="Open")
menubar2.add_command(label="Execute")
menubar2.add_command(label="Close")
menubar2.add_separator()
menubar2more = Menu(menubar2, tearoff=0)
menubar2more.add_command(label="X")
menubar2more.add_command(label="Y")
menubar2.add_cascade(label="Place", menu=menubar2more)
menu.add_cascade(label="File", menu=menubar2)
menubar1 = Menu(menu, tearoff=0)
menubar1.add_command(label="AAA")
menubar1.add_command(label="BBB")
menu.add_cascade(label="Triple",menu=menubar1)
root.config(menu=menu)

root.mainloop()