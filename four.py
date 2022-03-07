class library():
    def __init__(self,regno,place,lname):
        self.reg=regno
        self.pl=place
        self.ln=lname
class openAccount(library):
    def __init__(self,regno,place,lname,name,age,place1):
        self.regno1=regno
        self.place1=place
        self.lname1=lname
        self.name2=name
        self.age1=age
        self.pplace2=place1
    def display(self):
        print("Register number : ",self.regno1)
        print("Place : ",self.place1)
        print("Librarian Name : ",self.lname1)
        print("Name : ",self.name2)
        print("Age : ",self.age1)
        print("Place : ",self.pplace2)
rr=input("Enter the register number : ")
pp=input("Enter the place : ")
ll1=input("Enter the Librarian's name : ")
nn1=input("Enter the name : ")
aa1=int(input("Enter the  age : "))
pp2=input("Enter the place : ")
print("\nAccount details\n")
obj=openAccount(rr,pp,ll1,nn1,aa1,pp2)
obj.display()
