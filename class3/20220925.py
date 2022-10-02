"""
class Cars: # 創立類別
    # 建構式
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat
    # 方法
    def move(self,meter):
        print("My car moves "+str(meter)+" meters")

    # 方法(Method)
    def PrintAttribute(self):
        print("My car's color is "+str(self.color))
        print("My car has "+str(self.seat)+" seats")

audi = Cars("blue",4) # 創立物件
audi.move(5) # 呼叫方法

audi = Cars("blue",4) # 創立物件
audi.PrintAttribute()
"""

# print(isinstance(audi, Cars)) #判斷類別與物件的關係

"""
# 建立屬性
audi.color = "green" 
audi.seat = 4

# 呼叫屬性
print(audi.color)
print(audi.seat)
"""


class FullName:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def PrintMyName(self):
        print("My name is "+str(self.firstname)+", "+str(self.lastname))

Man1 = FullName("Andy", "Wang") # 創立物(件Man1)
Man2 = FullName("Lulu", "Cheng") # 創立物件(Man2)
Man1.PrintMyName() # 呼叫方法(Man1)
Man2.PrintMyName() # 呼叫方法(Man2)

"""
Man1 = FullName("Andy", "Wang")
Man2 = FullName("Lulu","Cheng")
print(Man1.firstname,Man1.lastname)
print(Man2.firstname,Man2.lastname)
"""