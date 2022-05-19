class soda:
    lemonade = 0
    gazovana = 0
    def __int__(self,g,l):
        self.lemonade = g
        self.lemonade = l
    def add(self):
        self.g += 10
        self.l += 1
        print(self.g)
        print(self.l)
    def show_my_drink(self):
        if self.l > 0 :
            print("Газова вода з {ДОБАВКА}",self.lemonade)
            print("{Звичайна  газована вода}", self.gazovana)
            show_my_drink = (self)
            print(show_my_drink,self)
        print("Робимо вам напій")
