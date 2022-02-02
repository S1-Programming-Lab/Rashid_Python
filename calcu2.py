import calcu1
calcu1.add(x,y)
calcu1.subtract(x,y)
calcu1.multiply(x,y)
calcu1.divide(x,y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(x, y))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(x, y))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(x, y))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(x, y))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
