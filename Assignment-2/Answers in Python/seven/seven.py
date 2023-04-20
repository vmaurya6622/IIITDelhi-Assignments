#see below for the bonus problem incorporated as a comment
print("What would you like to do ? ")
process=['1. Insert a new entry', '2. Delete an entry','3. Find all matching entries by giving a clue name', '4. Find the entry with a phone number or email','5. exit']
for i in process:
    print(i)
print() 

import json
file_location = r"E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\seven\addrbook.json"
listObj = []
record={}
file=open(file_location)
listObj = json.load(file)
# print(listObj)
file.close()
record |= listObj

# print(record)
counter=0
for i in record.keys():
    counter+=1

while True:
    user_input = int(input("Enter your choice by serial number (one at a time !) : "))
    if user_input==1:
        counter+=1
        allnames = []
        for i  in record.keys():
            allnames.append(i)
        allkeys = []
        for i in record.values():
            allkeys.append(i)
        print("You selected to add a new entry !")
        name = input("Enter Name : ")
        name.lower()
        address = input("Enter Address : ")
        address.lower()
        number = int(input("Enter Phone No. : "))
        email = input("Enter Email ID : ")
        email.lower()
        if name in allnames:
            index = allnames.index(name)
            local = str(allkeys[index])
            # lst = []
            if local[0] == "{":
                lst = []
                lst.append(allkeys[index])
                lst.append({"address":address,"phone No.":number,"email":email})
            else:
                lst = allkeys[index]
                lst.append({"address":address,"phone No.":number,"email":email})
                record[name]=lst
        else:
            record[name]={"address":address,"phone No.":number,"email":email}


        print(record)
        print("New entry named",name,"has been added successfully !")
        json_file=open(file_location,'w')
        json.dump(record, json_file,indent=4,separators=(',',': '))
        # print(type(record))
        json_file.close()

        
    if user_input == 2:
        print()
        print("Choose the serial no. at the left for the entry you want to delete. ")
        c=1
        for i in record:
            print(c,i)
            c+=1
        lst=[]
        for i in record.keys():
            lst.append(i)

        deleteLine=int(input("Enter the serial no. : "))
        print("The Entry named",lst[deleteLine-1],"has been deleted successfully !")

        file=open(file_location)
        data = json.load(file)
        data.pop(lst[deleteLine-1])

        with open(file_location, "w") as f:
            json.dump(data, f,indent=4,separators=(',',': '))
        f.close()    

    if user_input==3:
        lst = [i for i in record]
        name = input("Enter the Clue Name : ")
        length = len(name)
            
        for i in lst:
            if i[:length] == name:
                print(i,record[i])


    if user_input==4: 
        print()
        b=str(input("Enter the Phone Number / MailID : "))
        allnames=[]
        for i  in record.keys():
            allnames.append(i)
        c=[str(i) for i in record.values()]
        # r=c.find(b)
        m=0
        for i in c:
            r=i.find(b)
            if r !=-1:
                print(" Matches were found in the Addressbook as below :")
                m+=1
                k=0
                for t in c:
                    k=c.index(i)
                print(allnames[k],i)
            else:
                continue    
        if m==0:
            print("NO Mathches of the query were found in the addressbook.")    


    if user_input==5:
        # print(record)
        print("your Address Book has been closed !")
        file.close()
        break


#_________X___________________X___________________X___________________X___________________X___________________X___________________X__________
#bonus problem

# my_file="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\seven\Bonus\me.json"
# friend_file="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\seven\Bonus\myfriend.json"
# import json
# file = open(my_file)
# dicti = json.loads(file.read())
# file.close()
# # print(d)

# a = open(friend_file)
# dic = json.loads(a.read())
# a.close()

# mearge_file="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\seven\Bonus\mearged.json"
# k=dicti | dic
# #print(k,type(k))
# b=open(mearge_file,'w')
# json.dump(k, b,indent=4,separators=(',',': '))
# b.close()


