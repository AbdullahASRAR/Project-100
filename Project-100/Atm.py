class Atm(object):
    def __init__(self,cardNumber,PINNumber):
        self.cardNumber=cardNumber
        self.PINNumber=PINNumber
    def CashWithdrawl(self,amount):
        newAmount=50000-amount
        print("You withdrawed ",amount)
        print("aivilable balance is ",newAmount)
    def BalanceEnquiry(self):
        print("Your balance now isnow 50000")    
abdullah=Atm(5973646472,7586)
abdullah.BalanceEnquiry()     
abdullah.CashWithdrawl(25060)
   
            
