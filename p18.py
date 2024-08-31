#18.18. Write a Python program to find whether the given year is a leap year or not.
year=int(input("Enter year:"))
if(year%4==0):
    print(year," is leap year")
else:
    print(year," is not leap year")
'''
output:

Enter year:2028
2028  is leap year
>>>

Enter year:2027
2027  is not leap year
'''
