# population=int(input("Enter the initial population :- "))
# rate=float(input("Enter the Current Growth rate :- "))
#  i will define a function of increasing and decreasing population with a while loop and use it in the for loop to get the result.
# years=float(input("Enter the year 'n' :- "))
# population is increasing by 0.4% and decreasing by 0.1%
# part(1)
ppln=[50, 1450, 1400, 1700, 1500, 600, 1200] 
def sump(ppln):
    counter=0
    for i in ppln:
        counter+=i
    return(counter)
print("The total initital/current population of the world is :-",sump(ppln))  

# part(2)

growth = 2.5
constant=0 
years = 0
while (True):
    previous_year=0
    current_year=0
    def width(ppln):  
        counter=0 
        for i in ppln:
            counter+=1 
        return counter

    def population(ppln,growth_rate):
        grown_population = ppln+(ppln*(growth_rate/100))
        return grown_population


    for i in range(0,width(ppln)):
        growth_rate = growth-(0.4 * constant)
        constant += 1
        popl=population(ppln[i],growth_rate)
        previous_year += popl 
        ppln[i] = popl
    growth-=0.1    
    years+=1   
    constant=0
    for i in range(0,width(ppln)):
        growth_rate = growth - (0.4 * constant)
        constant += 1
        popl=population(ppln[i],growth_rate)
        current_year+=popl 

    constant=0
    if previous_year > current_year :
        print("Maximum population attained will be =",round(previous_year,2),"and in",years,"Years.")
        break 
    else:
        continue


