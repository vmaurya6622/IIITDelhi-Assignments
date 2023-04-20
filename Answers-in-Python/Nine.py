from math import exp                    #importing the exponential function of inbuilt math function of python
def demand(p):                          #defining the demand function
    m=exp(a-(b*p))
    return (m)
def supply(p):                          #defining the supply function
    q=exp(c+(d*p)) 
    return q
a=10
b=1.05
c=1
d=1.06
p=1                                    #setting initial price at 1 ATQ.
while True:
    if round(demand(p))-round(supply(p)) <= 0:       #checking where they actually cut/intersect each other.
        print("Price at equilibrium is :",round(p,3))
        print("Supply at equilibrium is :",round(supply(p),3))
        print("Demand at equilibrium is :",round(demand(p),3))
        break
    else:
        p+=0.05*p
        
        




