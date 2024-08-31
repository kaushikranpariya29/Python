num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if(num1>num2 and num1>num3):
    print(num1,"is maximum")
elif(num2>num1 and num2>num3):
    print(num2,"is maximum")
else:
    print(num3,"is maximum")
'''
output:
Enter num1: 12
Enter num2: 32
Enter num3: 33
33 is maximum
'''
