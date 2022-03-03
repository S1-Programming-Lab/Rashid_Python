import datetime
date=datetime.date.today()
currentYear=int(date.strftime("%Y"))
print("Enter the last year ")
endYear=int(input())
print("List of leap years ")
for year in range(currentYear,endYear):
    if((year%4==0)and(year%100!=0)or(year%400==0)):
        print(year)
