x=int(input("Enter the Value for Rows :- "))         # Input for the Number of rows
z=(2*x)+1                                            # doubling the x and adding 1 to it to get it suitable for the conditions
for i in range(1,x+1):                               # 
    for j in range(1,z):                             # 
        if j<=i or j>=z-i :                          # getting an optimum range to print the stars
            print("*",end="")                               
        else:                                        
            print(" ",end='')                        # calling this to print spaces in between the stars
    print()                                          # calling this to change line after every for loop in 'j'
