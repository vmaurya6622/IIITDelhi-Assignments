menu={'1. samosa':15,"2. Idli": 30, "3. Maggie": 50, "4. Dosa": 70, "5. Tea": 10, "6. Coffee": 20, "7. Sandwich": 35, "8. ColdDrink": 25,"9. Mangoshake":35}
for i,j in menu.items():
    print(i,"-",j,"/-")
order=[]
while True:
    ord=list(map(str,input("Please enter Serial <s> Quantity of item to order : ").split()))
    c=0
    for i in ord:
        if i.isdigit()==False:
            c+=1
        else:
            continue
    if ord==[]:
        break
    
    order.append(ord)
    if int(ord[0])>9:
        print()
        print("Give order for the listed items only according to the given serial numbers.")
        print()
        order.pop()
    if c>0:
        del order[-1]
        break        
print()
total=[]
for i in order:
    if int(i[0])==1:
        t=menu['1. samosa']*int(i[1])
        total.append(t)
        print("samosa",int(i[1]),'Rs',t)
    if int(i[0])==2:
        t=menu['2. Idli']*int(i[1])
        total.append(t)
        print("Idli",int(i[1]),'Rs',t)          
    if int(i[0])==3:
        t=menu['3. Maggie']*int(i[1])
        total.append(t)
        print("Maggie",int(i[1]),'Rs',t) 
    if int(i[0])==4:
        t=menu['4. Dosa']*int(i[1])
        total.append(t)
        print("Dosa",int(i[1]),'Rs',t) 
    if int(i[0])==5:
        t=menu['5. Tea']*int(i[1])
        total.append(t)
        print("Tea",int(i[1]),'Rs',t) 
    if int(i[0])==6:
        t=menu['6. Coffee']*int(i[1])
        total.append(t)
        print("Coffee",int(i[1]),'Rs',t) 
    if int(i[0])==7:
        t=menu['7. Sandwich']*int(i[1])
        total.append(t)
        print("Sandwich",int(i[1]),'Rs',t) 
    if int(i[0])==8:
        t=menu['8. ColdDrink']*int(i[1])
        total.append(t)
        print("coldDrink",int(i[1]),'Rs',t) 
    if int(i[0])==9:
        t=menu['9. Mangoshake']*int(i[1])
        total.append(t)
        print("Mangoshake",int(i[1]),'Rs',t) 
    else:
        continue
count=0
for i in total:
    count+=i

item=0 
for i in order:
    item+=int(i[1])


print()
print("Your billing Invoice is listed below :")    
print("Total",',',item,'Items','Rs',count)            

















