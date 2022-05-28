class Client:
    #public - публічний
    #protected - захищений
    #dpivate - приватний
    def __init__(self,name,balance,creditBalance, passport):
        self.__name = name
        self.__balansDanFunds = balance
        self.__balansCreditFunds = creditBalance
        self.__passport = passport
    def addDanFunds(self,money):
        self.__balansDanFunds =+ money
    def addCreditFunds(self,money):
        self.__balansCreditFunds =+ money
    #def printProtectedData(self):
        #print(self.name,self.balansDanFunds,self.balansCreditFunds,self.passport)
    def printPriveteDate(self):
        print(self.name, self.balansDanFunds, self.balansCreditFunds, self.passport)


account1 = Client("Bob",1000,300,56784398)
account1.printPriveteDate()
#print(account1.__name)
#print(account1.__balansDanFunds)
#print(account1.__balansCreditFunds)
#print(account1.__passport)


