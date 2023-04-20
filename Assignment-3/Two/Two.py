x=["show the record of particular student moving in/out of campus.","Giving the start time and the end time (in 24hr format) as input \nto get all the students who entered/exited the campus during this time.","Giving the gate number to determine the number of times students have entered/exited the campus through that gate.","Exit"]
print("Choose an option for the task !")
for i in range(len(x)):
    print(f"({i+1}) {x[i]}")

file_location=r"E:\One Drive\OneDrive - indraprashtha institute of information technology\IIITD Projects\IP\Project assignment - 3\two\data.txt"
file=open(file_location,'r+')
number_of_lines= int(len(file.readlines()))
file.seek(0,0)               #seeking to 0,0 bcs no. of lines command has sent the line reader to end.
file.readline()           # to start the data reading from line 2 of data.txt

data={}
file_output=r"E:\One Drive\OneDrive - indraprashtha institute of information technology\IIITD Projects\IP\Project assignment - 3\two\output.txt"

for i in range(number_of_lines):
    dic={}
    value = file.readline().strip().split(", ")
  
    if value[0]=='':
        break
    d={"types":value[1],"gate":value[2],"time":value[3]}
    data[value[0]]=d

ta_names=[i for i in data.keys()]

file.seek(0,0)
file.readline()

part3=[]
part1=[]


bunch_data={}
for i in range(len(ta_names)):
    types=[]
    gate=[]
    time=[]
    k=[]
    n=ta_names[i]
    value=[]
    for j in range(number_of_lines):
        value = file.readline().strip().split(", ")  #for i in number_of_lines]
        
        if value[0] == n:
            types.append(value[1])
            gate.append(int(value[2]))
            time.append(value[3].split(":"))
            # k=
            C=[value[1],int(value[2]),value[3].split(":")]
            k.append(C)
        else:
            continue
    for d in range(len(k)-2):
        m1 = k[d][0]
        m2 = k[d+1][0]
        if (m1 == "ENTER" and m2 =="ENTER") or (m1=="waste" and m2=="ENTER"):
            k[d+1] = ["waste"]
        elif (m1=="EXIT" and m2=="EXIT") or (m1=="waste" and m2=="EXIT"):
            k[d]=["waste"]
    
    l=[]
    for b in range(len(k)):
        t=k[b]
        if len(t)==3:
            l.append(t)

    bunch_data[n]=l 
    for e in l:
        # print(e[2])
        w=[int(i) for i in e[2]]
        # print(w)
        y=[e[0],w]
        part1.append(y)  

    for h in l:
        q=[h[0],h[1]]
        part3.append(q)
    file.seek(0,0)
    file.readline()
    types.clear()
    gate.clear()
    time.clear()
    
gates={}
type_entry={}
time_entry={}
for i in bunch_data.keys():
    l=[]
    m=[]
    n=[]
    o=bunch_data[i]
    for j in o:
        l.append(j[1])
    
    for k in o:
        m.append(k[0])
    
    for e in o:
        n.append([int(p) for p in e[2]])

    type_entry[i]=m
    time_entry[i]=n
    gates[i]=l
reqdata={}
for i in ta_names:
    k=bunch_data[i]
    
    t=[j[0] for j in k]
    # print(t)
    g=[j[1] for j in k]
    ty=[j[2]for j in k]
    tym=[]
    for y in ty:
        m=":".join(j for j in y)
        tym.append(m)
    reqdata[i]={"types":list(t),"gate":list(g),"time":list(tym)}
    

# print(reqdata)
while True:
    user_inp=input("Enter your Choice here :- ")
    try:
        if int(user_inp) == 1:
            # print(ta_names)
            for i in ta_names:
                print(i,end=', ')
            print()
            print()
            name=str(input("Please Enter the Student Name you want to search: "))
            try:
                t=type_entry[name]
                g=gates[name]
                tym=time_entry[name]
                # print(tym)
                u=[]
                for i in tym:
                    x=":".join(str(j) for j in i)
                    u.append(x)
                data=[]
                for i in range(len(t)):
                    c=(t[i],g[i],u[i])
                    data.append(c)
                
                with open(file_output,'w') as f:
                    f.write(str(list((name,data))))
                f.close()
                print("Successfully printed about the data of",name,"in the output.txt")
                print()
                curr_time=input("Please Enter the current time : ")
                types=reqdata[name]["types"]
                time=reqdata[name]["time"]
                g=[]
                for i in time:
                    if i<=curr_time:
                        g.append(i)
                index=len(g)-1
                if types[index]=="ENTER":
                    print("The student is inside the Institute.")
                else:
                    print("The student is outside the Institute.")    
                # print(types,time)
                # print(g,index)

            except:
                print("Entry not found in the file...")
        if int(user_inp) == 2:
            start=input("Enter the start time :- ")
            end=input("Enter the end time :- ")
            f=open(file_output,"w")
            f.write(f'TA, Crossing, Gate number, Time\n')
            for i in reqdata:
                for j in range(len(reqdata[i]["time"])):
                    if end>=reqdata[i]["time"][j]>=start:
                        p=""
                        p=p + f'{i},{reqdata[i]["types"][j]} ,{reqdata[i]["gate"][j]}, {reqdata[i]["time"][j]}'+"\n"
                        f.write(p)
            print("The entries between",start,"and",end,"has been printed in the output file.")            
            f.close()          
        if int(user_inp) == 3:
            gate=int(input("Enter the gate no. to query :- "))
            enter_counter=0
            exit_counter=0
            for i in part3:
                if i[0]=="ENTER" and i[1]==gate:
                    enter_counter+=1
                elif i[0] == "EXIT" and i[1]==gate:
                    exit_counter+=1
                else:
                    continue
            print(f"From gate no. {gate} total number of 'Entries' recorded are : {enter_counter}.")
            print(f"From gate no. {gate} total number of 'Exits' recorded are : {exit_counter}.")
        if int(user_inp)==4:
            print("You have Successfully Exited !")
            break    
    except:
        pass
    if user_inp=="":
        print("You have successfully exited!")
        break

