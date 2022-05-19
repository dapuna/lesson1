class cat:
    hp = 100
    eat = 100
    name = "Masha"
    def __int__(self,n):
        self.name = n
        print(self.name,"hello")
        self.live()
        self.live()
        self.eateng()
    def eateng(self):
        self.eat  += 10
        print(self.eat)
    def live(self):
        self.eat -=5
        print(self.eat)
    def damsge(self):
        self.ho -=25
weywuxian = ("Masha")