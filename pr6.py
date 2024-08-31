principal = float(input('Enter amount: '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))

si = (principal*time*rate)/100
ci = principal * ( (1+rate/100)**time - 1)

print("Simple interest is: ",si)
print("Compound interest is: ",ci)
