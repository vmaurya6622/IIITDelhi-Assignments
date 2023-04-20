marks=[]
while True:
    x=list(map(str,input("Enter course_no <s> number_of_credits <s> grade_received : ").split()))    #<s> for entering space separated input
    x=list(x)
    if x==[]:
        break
    if x[0].isalnum == False:
        print("Improper Course Number.")
        break
    
    if int(x[1]) == 1 or int(x[1]) ==2 or int(x[1]) == 4 :
        pass
    else:
        print("Incorrect Credit Entry")
        break
    if x[2] =='A+' or x[2] =='A' or x[2] =='B' or x[2] =='B-' or x[2] =='C' or x[2] =='C-' or x[2] =='D' or x[2] =='F' or x[2] =='A-':
        pass
    else:
        print("Incorrect Grade entry.") 
        break  
    marks.append(x)
courses=[]
for i in marks:
    courses.append(i[0])

credit=[]
for i in marks:
    credit.append(i[1])  

allott={"A+":(10), "A":(10), "A-":(9), "B":(8), "B-":(7), "C":(6), "C-":(5), "D":(4), "F":(2)}
grade=[]
for i in marks:
    c=allott[str(i[2])]
    grade.append(c)

mk=marks
for i in mk:
    del i[1]    
for i in mk:
    for j in i:
        print(j+"  " ,end=' ')
    print()
    
m=0
def sgpa(m):
    k=0
    for i in range(len(marks)):
        k+=int(credit[i])*int(grade[i])
    s=0
    for i in credit:
        s+=int(i)
    p=round(k/s,2)    
    return(p)

print("SGPA of the student is :",sgpa(m))    

