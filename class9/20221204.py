from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Class9")
root.geometry("400x400+150+200")

"""
# 宣告文字變數
val = StringVar()
# 放入第一個單選按鈕
Radiobtn1 = Radiobutton(root, text="Black", variable=val, value="Black")
Radiobtn1.pack()
# 指定選取第一單選按鈕
Radiobtn1.select()
# 放入第二個單選按鈕
Radiobtn2 = Radiobutton(root, text="Red", variable=val, value="Red")
Radiobtn2.pack()
"""
"""
def ClickRadiobtn1():
    Label_Choose["fg"] = "Blue"
    Label_Choose["textvariable"] = val
def ClickRadiobtn2():
    Label_Choose["fg"] = "Green"
    Label_Choose["textvariable"] = val
def ClickRadiobtn3():
    Label_Choose["fg"] = "Pink"
    Label_Choose["textvariable"] = val

val = StringVar()
Label_Title = Label(root, text="Please select the color you prefer")
Label_Title.pack()
Radiobtn1 = Radiobutton(root, text="Blue", variable=val, value="Blue", fg="Blue", command=ClickRadiobtn1)
Radiobtn1.pack()
Radiobtn2 = Radiobutton(root, text="Green", variable=val, value="Green", fg="Green", command=ClickRadiobtn2)
Radiobtn2.pack()
Radiobtn2.select()
Radiobtn3 = Radiobutton(root, text="Pink", variable=val, value="Pink", fg="Pink", command=ClickRadiobtn3)
Radiobtn3.pack()
# 顯示被選取按鈕之value
Label_Choose = Label(root, textvariable=val, font=("Arial",30))
Label_Choose.pack()
"""
# """
def CreateNewWindow():
    # 建立新視窗 New Windows
    NewWindows = Toplevel(root)
    # 建立 Label 在 New Windows 裡
    Label_Message = Label(NewWindows, text="New Window")
    Label_Message.pack()

    # 建立 Button 在 New Windows 裡
    # Button_NewWindow = Button(NewWindows, text="New Window Button")
    # Button_NewWindow.pack()

    # 建立 Destroy Button 在 New Windows 裡
    DestroyBtn = Button(NewWindows, text="Quit", command=NewWindows.destroy)
    DestroyBtn.pack()

    # 建立 Hide Button 在 New Windows 裡
    HideBtn = Button(NewWindows, text="Hide", command=root.iconify)
    HideBtn.pack()
    
    # 建立 Show Button 在 New Windows 裡
    ShowBtn = Button(NewWindows, text="Show", command=root.deiconify)
    ShowBtn.pack()

    # 建立 Withdraw Button 在 New Windows 裡
    WithdrawBtn = Button(NewWindows, text="Withdraw", command=root.withdraw)
    WithdrawBtn.pack()

    # 執行新視窗程式
    NewWindows.mainloop()

# 點擊 Button 產生 New Windows
CreateNewWindowBtn = Button(root, text="Click to Create New Windows!", command=CreateNewWindow)
CreateNewWindowBtn.pack()
"""
"""
# *args 可變參數
def function(m, *args):
    print(m)
    print(args)

# 呼叫執行 function ，並給多個(>2個)參數值傳入該funtion
# 除了 1 為參數 n 外，其餘都是 *args 的輸入質
function(1,2,3,4,5,6,7)

def function(*args, **kwargs):
    print(kwargs)
    print(args)

# 呼叫執行 function ，並給多個(>2個)參數值傳入該funtion
# 前四個值為*args可變參數，後兩個值為 **kwargs 關鍵字可變參數
function(1,2,3,4, num1=5,num2=10)
# """

# val = StringVar()
# def CreateNewWindow():
#     NewWindows = Toplevel(root)
#     def ClickRadiobtn1():
#         Label_Choose["fg"] = "Blue"
#         Label_Choose["textvariable"] = val
#     def ClickRadiobtn2():
#         Label_Choose["fg"] = "Green"
#         Label_Choose["textvariable"] = val
#     def ClickRadiobtn3():
#         Label_Choose["fg"] = "Pink"
#         Label_Choose["textvariable"] = val
#     Label_Title = Label(NewWindows, text="Please select the color you prefer")
#     Label_Title.pack()
#     Radiobtn1 = Radiobutton(NewWindows, text="Blue", variable=val, value="Blue", fg="Blue", command=ClickRadiobtn1)
#     Radiobtn1.pack()
#     Radiobtn2 = Radiobutton(NewWindows, text="Green", variable=val, value="Green", fg="Green", command=ClickRadiobtn2)
#     Radiobtn2.pack()
#     Radiobtn2.select()
#     Radiobtn3 = Radiobutton(NewWindows, text="Pink", variable=val, value="Pink", fg="Pink", command=ClickRadiobtn3)
#     Radiobtn3.pack()
#     Label_Choose = Label(NewWindows, textvariable=val, font=("Arial",30))
#     Label_Choose.pack()

# CreateNewWindowBtn = Button(root, text="Start", command=CreateNewWindow)
# CreateNewWindowBtn.pack()


root.mainloop()