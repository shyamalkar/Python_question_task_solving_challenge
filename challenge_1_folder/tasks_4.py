num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter second integer: "))

result = (num1 > 10 and num2 > 10 and 
          ( num1 % 2 == 0 or num2 % 2 == 0))
print(result)


