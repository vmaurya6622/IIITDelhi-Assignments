wts = [[10, 5], [20, 5], [60, 15], [40, 10],[15,10],[20,5],[30,20],[15,10],[30,15],[10,5]]
number_of_students = 5

file_location="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\six\IPmarks.txt"
write_file_location="E:\IIITD Projects\IP\Project assignment - 2\Vishal Kumar Maurya\Answers\six\IPgrades.txt"

file=open(file_location)

student_list=[]
for i in range(number_of_students):
    k=file.readline().strip().split( ',' )
    student_list.append(k)

file.close()

student_grades=[]
for i in student_list:
    a1=(float(i[1])/10)*5
    a2=(float(i[2])/20)*5
    a3=(float(i[3])/60)*15
    a4=(float(i[4])/40)*10
    a5=(float(i[5])/15)*10
    a6=(float(i[6])/20)*5
    a7=(float(i[7])/30)*20
    a8=(float(i[8])/15)*10
    a9=(float(i[9])/30)*15
    a10=(float(i[10])/10)*5
    marks=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
    student_grades.append(round(marks,4))
    marks=0

roll_no=[]
for i in student_list:
    k=i[0]
    roll_no.append(k)


given_grades=[]
for i in student_grades:
    if i > 80 :
        given_grades.append("A")
    if i <= 80 and i > 70 :
        given_grades.append("A-")
    if i <= 70 and i > 60 :
        given_grades.append("B")
    if i <= 60 and i > 50 :
        given_grades.append("B-")
    if i <= 50 and i > 40 :
        given_grades.append("C")
    if i <= 40 and i > 35 :
        given_grades.append("C-")
    if i <= 35 and i > 30 :
        given_grades.append("D")
    if i <= 30 :
        given_grades.append("F")

print('Following will be Written !')
print()
write_file=open(write_file_location,'w')
for i in range(number_of_students):
    k=('Roll No.: '+str(roll_no[i])+'  Total Marks: '+str(student_grades[i])+'  Grade: '+str(given_grades[i]))
    
    print(k)
    write_file.write(str(k))
    write_file.write('\n')

write_file.close()
print()
print("All Tasks Done You can check the File.")
