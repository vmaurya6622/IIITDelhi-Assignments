distance_traversed=0      #Setting initial distance to '0'.
abscissa=0
ordinate=0
while True:               #making while loop True for every condition until the condition breaks.
    x=float(input("Enter the distance traversed :- "))
    if x<=0:
        break
    else:
        if x <= 25:        # stating for North Direction
            distance_traversed += x
            ordinate += x

        elif 25<x<=50:            # Stating for south Direction.
            distance_traversed += x
            ordinate -= x

        elif 50<x<=75:            # Stating for east Direction.
            distance_traversed += x
            abscissa += x

        elif x>75:            # Stating for west Direction.
            distance_traversed += x
            abscissa -= x  

    final_coordinates = (round(abscissa),round(ordinate))            
    total_displacement = ((abscissa)**2 + (ordinate)**2)**0.5
    print("Coordinates of the vehicle are : " , final_coordinates)
    print("Total Distance Traversed : "+ str(distance_traversed))
    print("Displacement of the vehicle : "+str(round(total_displacement,3)))