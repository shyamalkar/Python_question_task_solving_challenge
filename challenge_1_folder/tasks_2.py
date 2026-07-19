#operator precedence demonstration

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter e: "))

# standard precedence

result1 =  a * b + c/ d - e
print("Result using standard precedence:", result1)


# changed order using parentheses
result2 = ( a * ( b + c)) / ( d - e )
print("Result using parentheses:", result2)

