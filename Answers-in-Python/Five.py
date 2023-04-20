def factorial(n):         #calculating factorial to take them in the infinite series in the numerator
    value = float(1)
    for i in range(1, n+1):
        value = value * i
    return value

def sin(x):
    x = x * 3.1415/180      # Exchanging value from degrees to radians
    value = x               # setting value == x (now in radians) to get startd by it
    negative_sign = -1               
    n = 200                 # precision of the sin (x) is defined here.
    i = 3
    while i < n:
        value = value + (pow(x, i)/factorial(i) * negative_sign)
        i = i + 2           # incrementing the value of i by 2 so  that it goes at odd terms of powers like 1,3,5,7.... 
        negative_sign *= -1    # to change sign at every alternate position
    return value

def cos(x):
    x = x * 3.1415/180      # Exchanging value from degrees to radians
    value = 1               # the expansion starts from 1 rather x like in sin (x) therefore setting value of first variable as 1
    negative_sign = -1               
    n = 200                 # precision of the cos (x) is defined here.
    i = 2
    while i < n:
        value = value + (pow(x, i)/factorial(i) * negative_sign)
        i = i + 2           # incrementing the value of i by 2 so  that it goes at odd terms of powers like 0,2,4,6,8.... 
        negative_sign *= -1    # to change sign at every alternate position
    return value  

x=float(input("Enter the Angle Of Elevation :- "))
b=float(input("Enter the 'Length' from the person to the pole :- "))
y=round(sin(x),3)
z=round(cos(x),3)
tan_x=round((y/z),3)
perpendicular=round((tan_x*b),3)
hypotenuse=round(((perpendicular**2+b**2)**0.5),3)          # Evaluating the hyponenuse by pythagoras and rounding off the value to 3 values
print("Height of the pole is "+str(perpendicular)+" metre "+ "and distance to the top of the pole from the person is "+str(hypotenuse)+ " metre.")


