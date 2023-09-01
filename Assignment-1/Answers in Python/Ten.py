def value(x0):              #defining the function for the values @ X0
    a=x0**3-10.5*(x0**2)+34.5*x0 - 35
    return (a)
def differentiation(x0):    #defining the function for the values of differentiation of X0 @ X0.
    b=3*x0**2-21*x0+34.5
    return (b)    
x0=int(input("Enter the value of x0 :- "))      #inputting the values of guess
expansion=0.2   
while abs(value(x0))>expansion:                 #iterating using the while near the X0 by getting its  values @ value(X0) and differentiation(x0)
    x0=x0-(value(x0))/differentiation(x0)
print(round(x0,3))
for i in range(1500):                           #making the function more precise about finding the roots by increasing the loop counts.
    x1=x0-(value(x0))/differentiation(x0)       #increasing the values of X0 and usnig it as a next guess.
    if abs(x1-x0)<expansion:
        print(round(x1,3))
        break
    x0=x1
        
