class VideoGame:
    def __init__(self,Game,Time):
        self.Game = Game
        self.Time = Time

    def Play(self):
        print("The game is "+str(self.Game)+" usually play "+str(self.Time)+" min")

Man1 = VideoGame("MC","90") # 創立物件
Man1.Play() # 呼叫方法