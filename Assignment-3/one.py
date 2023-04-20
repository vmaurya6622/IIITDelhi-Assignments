# x = 6     
x = int(input("Enter the Value for Rows :- "))             # Input for the columnber of rows
print("The required pattern is printed below !")
print()

# function to print upper part of the pattern
def upperpart(x):
    def print_stars(star):
        if (star == 0):
            return
        print("* ", end = "")
        print_stars(star-1 )
    
    def print_spaces(space):
        if (space == 0):
            return
        print(" ", end = "")
        print(" ", end = "")
        print_spaces(space - 1)
    
    def pattern(n, column):     #recursively printing stars and spaces line by line
        if (n == 1):
            return
        print_stars(n)
        print_spaces(2 * (column - n) )
        print_stars(n)
        print("")
        pattern(n-1 , column)
    pattern(x, x)



#function to print the lower part of the pattern
def lowerpart(x):
    def print_stars(star):
        if (star == 0):
            return
        print("*", end = " ")
        print_stars(star - 1)
    
    def print_spaces(space):
        if (space == 0):
            return
        print(" ", end = "")
        print(" ", end = "")
        print_spaces(space-1)
    
    def pattern(n, column):
        if (n == 0):
            return
        print_stars(column-n+1)
        print_spaces((2*n)-2)
        print_stars(column-n+1)
        print()
        pattern(n-1,column)
    
    pattern(x, x)
#calling functions to get the output      
upperpart(x)
lowerpart(x)