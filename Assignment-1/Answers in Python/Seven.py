laptop_cost=float(input("Cost of Laptop :- "))        # inputting the required values
allowance=float(input("Allowance :- "))
sf=float(input("Your Saving Fraction :- "))
r=float(input("Rate of interest :- "))
months=0                                               # setting months to 0to start initially
savings=(allowance)*sf
while True:
    if savings<=laptop_cost:                           # constraint to run the function to reach the output
        def compound(savings):                         # defining the compound interest
            amount=(savings*((1+r/12)**(1)))-savings
            return amount
        savings+=compound(savings)              
        savings+=(allowance)*sf                       #chaning the values of saivng and months after every iteration under while loop
        months+=1
        
    else:                                
        print("Numbers of required months are :- ",(months-1))
        print("Total savings are :- ",round(savings-laptop_cost,3))
        break                           #breaking after the IF condition gets false