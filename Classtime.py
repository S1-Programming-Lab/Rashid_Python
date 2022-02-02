class time:
    def __init__(self,h,m,s):
        self.hr=h
        self.min=m
        self.sec=s
    def __add__(self,other):
        tempsec=self.sec+other.sec
        tempmin=tempsec/60
        self.sec=int(tempsec%60)
        self.min=self.min+other.min+tempmin
        temphr=self.min/60
        self.min=int(self.min%60)
        self.hr=int(self.hr+other.hr+temphr)
        return time(self.hr,self.min,self.sec)
    def __str__(self):
        return (str(self.hr)+'hr'+str(self.min)+'min'+str(self.sec)+'sec')
a=int(input("Enter Hour of t1:"))
b=int(input("Enter mintue of t1:"))
c=int(input("Enter second of t1:"))
x=int(input("Enter Hour of t2:"))
y=int(input("Enter mintue of t2:"))
z=int(input("Enter Second of t2:"))
t1=time(a,b,c)
t2=time(x,y,z)
print(t1+t2)
