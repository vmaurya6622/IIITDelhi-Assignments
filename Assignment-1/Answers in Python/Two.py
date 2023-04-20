m=int(input("Enter the value of 'M' :- ")) # inputting the values of M
# assigning x1 for Tables
# assigning x2 for Chairs
# 8x1+2x2=400 constraint for Table
# 2x1+x2=120 Constraint for Chair
# import math
# import numpy as np
# x1=np.array([8,2],[2,1])
# x2=np.array([400,120])
# np.linalg.solve(x1,x2)
def f(x1):                     #defining the Contraints for X1
    x1=(400-2*x2)/8
    return (x1)
def f(x2):                      #defining the constraints for x2
    x1=(120-x2)/2
    return (x1)
x2=0
x1=0
while True:
    if x1==f(x1) and x1==f(x2):                 # Solving the linear equations by using the while loop
        print("Number of tables are :",x1,"Number of chairs are :",x2)
        profit=m*90+(x1-m)*100+m*25+(x2-m)*30        #according to the question finding the value of profit according to the values of 'M'
        print("Total profit is :- ",profit)
        break
    else:                                   #if the values didn't match then it will iterate again by increading its values by 1.
        x1+=1
        x2+=1

# print("Number of tables are :",x1,"Number of chairs are :",x2)
# profit=x1*m*90+x1*(x1-m)*100+x2*m*25+x2*(x2-m)*30
# print("profit")
