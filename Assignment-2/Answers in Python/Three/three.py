file=open(r"E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\Three\sample_dict.txt")
yearbook = {}
Number_of_students = 6 #int(input("Enter the number of students : "))

for i in range(Number_of_students):

    dic={}
    c=(str(file.readline().strip()))
    d=c[:-1]                                     #taking the strings (-1) from last as the name at ending has ':'
    for j in range(Number_of_students-1):
        value = file.readline().strip().split(",")
        dic[str(value[0])] = int(value[1])                   #appending in the dictionary the values of students
    yearbook[d] = dic

# print(yearbook)
sum=[]
t=0
for m in yearbook.keys():    
    for i in yearbook[m]:
        k=yearbook[m][i]
        if k == 1:
            t+=1
    sum.append(t)
    t=0    

# print(sum)
lmax=max(sum)
lmin=min(sum)

lst=[]
for i in yearbook.keys():
    lst.append(i)

max_values = max(sum)
max=[index for index, item in enumerate(sum) if item == max_values]

for i in (max):
    k=lst[i]
    print("The student who has got 'maximum' signature is",k,"with",lmax,'signatures')

    
print()

min_values = min(sum)
min=[index for index, item in enumerate(sum) if item == min_values]

for i in (min):
    k=lst[i]
    print("The student who has got 'minimum' signature is",k,"with",lmin,'signatures')

file.close()
