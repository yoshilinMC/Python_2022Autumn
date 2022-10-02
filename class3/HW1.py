class People:
    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age

    def Print(self):
        print("My height is "+str(self.height)+" My weight is "+str(self.weight)+" My age is "+str(self.age))

Man1 = People(170,70,50) # 創立物件
Man1.Print() # 呼叫方法
WoMan1 = People(160,45,40) # 創立物件
WoMan1.Print() # 呼叫方法
Man3 = People(160,40,12) # 創立物件
Man3.Print() # 呼叫方法