class bank():
    def __init__(self,acc,name,typ,amt):
        self.ac=acc
        self.name=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("Account Holder name: ",self.name)
        print("Account Number: ",self.ac)
        print("Account Type: ",self.type)
        print("Account Amount: ",self.amount)
    def withl(self,wl):
        m=self.amount-wl
        return(m)
n=input("Enter A/c Holder Name:")
t=input("Enter A/c type:")
a=int(input("Enter A/c number:"))
am=int(input("Enter Amount to deposit:"))
obj=bank(a,n,t,am)
print("account Details")
obj.printamt()
w=int(input("Enter amount to withdraw:"))
print("balance=",obj.withl(w))
    
