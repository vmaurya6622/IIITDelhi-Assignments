starting_time=float(input("Enter the starting time 'a' :- "))
end_time=float(input("Enter the End time 'b':- "))
v0=0
v1=0
distance=0
while True:
    if starting_time>=end_time:
        print("Total Distance covered by a rocket between time a and b is :-",round(distance,3))
        break
    else:
        def intg(v):
            import math
            from math import log
            v = (2000*(log(140000/(140000-2100*starting_time)))-9.8*starting_time)
            return(v) 
        v0+=intg(starting_time)
        starting_time+=0.25
        v1+=intg(starting_time)
        avg_velocity=(v0+v1)/2
        distance += avg_velocity*0.25
        v0=0
        v1=0

 

        
    

