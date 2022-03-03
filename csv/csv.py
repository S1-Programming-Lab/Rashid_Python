importcsv
while open('emploee.csv',newline='')as csvfile1:
data=csv.Dictreader(csvfile1)
print("empnoname")
print(".........")
for i in data:
print(i['empno'],i['name'])
