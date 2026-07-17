# password complexity checker 

# password

password = input("Enter a password:")
result = len(password) > 8 and password[0].isalpha()
print(result)