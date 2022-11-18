from tkinter import *

# 建立主視窗
root = Tk()

# 設定視窗標題
root.title("HW5_3")

# 設定視窗座標位置
root.geometry("250x150")

# Label 標籤
mylabel = Label(root, text="三人坐沙發 綠色/灰色/黑色")
mylabel.pack(pady=20)
# Label2 標籤
mylabel2 = Label(root, text="NT.28,900")
mylabel2.pack(pady=20, side="left")
# buttom 按鈕
MyButton = Button(root, text="+")
MyButton.pack(pady=10, side="right", ipadx=10)
# Label3 標籤
mylabel3 = Label(root, text="0")
mylabel3.pack(pady=20, side="right", ipadx=5)
# buttom2 按鈕
MyButton2 = Button(root, text="-")
MyButton2.pack(pady=10, side="right", ipadx=10)

# 執行主程式
root.mainloop()