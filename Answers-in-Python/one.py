x=int(input("Enter the Number :- "))
#taking input from the user to convert it into number form
lst=["Zero","one","Two","Three","Four","Five","Six","Seven","Eight","Nine"]   #appending the numberes as a list
x=str(x)
if len(x)==1:           # according to the length of the input defining the functions
    if x=="0":
        print(lst[0])
    elif x=="1":
        print(lst[1])
    elif x=="2":
        print(lst[2])
    elif x=="3":
        print(lst[3])
    elif x=="4":
        print(lst[4])
    elif x=="5":
        print(lst[5])
    elif x=="6":
        print(lst[6])
    elif x=="7":
        print(lst[7])
    elif x=="8":
        print(lst[8])
    elif x=="9":
        print(lst[9])
if len(x)==2:                     # defining different conditions according to input i.e one/two digit inputs..
    if x=="10":
        print("Ten")
    elif x=="11":
        print("Eleven")
    elif x=="12":
        print("Twelve")
    elif x=="13":
        print("Thirteen")
    elif x=="14":
        print("Fourteen")
    elif x=="15":
        print("Fifteen")
    elif x=="16":
        print("Sixteen")
    elif x=="17":
        print("Seventeen")
    elif x=="18":
        print("Eighteen")
    elif x=="19":
        print("Nineteen")
    elif x=="20":
        print("Twenty")
if int(x)>=21 and int(x)<=99:
    for i in x[0]:
        if i == "2":
            print("Twenty",end=' ')
        elif i=="3":
            print("Thirty",end=' ')
        elif i=="4":
            print("Forty",end=' ')
        elif i=="5":
            print("Fifty",end=' ')
        elif i=="6": 
            print("Sixty",end=' ')
        elif i=="7":
            print("Seventy",end=' ')
        elif i=="8":
            print("Eighty",end=' ')
        elif i=="9":
            print("Ninety",end=' ')
    for o in x[1]:                  
        if o=="0":
            print(lst[0])
        elif o=="1":
            print(lst[1])
        elif o=="2":
            print(lst[2])
        elif o=="3":
            print(lst[3])
        elif o=="4":
            print(lst[4])
        elif o=="5":
            print(lst[5])
        elif o=="6":
            print(lst[6])
        elif o=="7":
            print(lst[7])
        elif o=="8":
            print(lst[8])
        elif o=="9":
            print(lst[9])
    
    

