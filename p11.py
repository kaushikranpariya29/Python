#Write a Python program to find remainder of division operation where the
#dividend and divisor are both natural number.

dividend = int(input("enter divident number:"))
divisor = int(input("enter divisor number:"))
if(dividend > 0 and divisor > 0):
    rem = dividend % divisor
    print("reminder is:",rem)
else:
    print("both are not natural number")


"""
enter divident number:20
enter divisor number:2
reminder is: 0
