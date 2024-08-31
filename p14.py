"""
14.
Write a Python program to find profit or loss based on cost price and sell price
of an item. Also print profit or loss percentage. (Profit and loss must be
positive number only)
"""
cost = int(input("enter cost price:"))
sell = int(input("enter sell price:"))
if(cost<sell):
     profit=sell-cost
     PP=(profit*100)/cost
     print("profit:",profit , "/n profit percentage:",PP)
else:
    loss=cost - sell
    CP= (loss*100)/sell
    print("loss:",loss,"rs" , "/n loss percentage:",CP)


"""
enter cost price:500
enter sell price:200
loss: 300 rs /n loss percentage: 150.0
