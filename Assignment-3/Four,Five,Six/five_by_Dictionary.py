#project 2 que (6) has same code
import time
start_time=time.time()


task=["(1). Create a course","(2). Add students marks for the assessments","(3). Exit."]
print("Choose an appropriate task no. to perform ... ")
for i in task:
    print(i)
file_location = r"E:\IIITD Projects\IP\Project assignment - 3\Four,Five,Six\IPmarks.txt"
grades_file=r"E:\IIITD Projects\IP\Project assignment - 3\Four,Five,Six\five\output.txt"
cutoffpolicy=[]

def create_course(cname, credits, assessments, policy):
    course = {
        "cname": cname,
        "credits": credits,
        "assessments": assessments,
        "policy": policy,
        "students": {}
    }
    # print(course)
    return course

def upload_marks(course, file_location):
    with open(file_location, 'r') as f:
        for line in f:
            data =[float(i) for i in  line.strip().split(",")]
            rollno = int(data[0])
            marks = [float(mark) for mark in data[1:]]
            total_marks = sum(marks)
            course["students"][rollno] = {"marks": marks, "total_marks": total_marks}

def do_grading(course):
    # print(course)
    policy = course["policy"]
    A=[]
    B=[]
    C=[]
    D=[]
    F=[]
    for rollno, student in course["students"].items():
        total_marks = student["total_marks"]
        if policy[0]-2 <= total_marks <= policy[0]+2:
            A.append(total_marks)
        if policy[1]-2 <= total_marks <= policy[1]+2:
            B.append(total_marks)   
        if policy[2]-2 <= total_marks <= policy[2]+2:
            C.append(total_marks)
        if policy[3]-2 <= total_marks <= policy[3]+2:
            D.append(total_marks) 
        if policy[4]-2 <= total_marks <= policy[4]+2:
            F.append(total_marks)    
    A.sort()
    B.sort()
    C.sort()
    D.sort()
    F.sort()
    A.insert(0,"A")
    B.insert(0,"B")
    C.insert(0,"C")
    D.insert(0,"D")
    F.insert(0,"E")
    policy_adopted={"A":80,"B":"Between 80 and 65","C":"Between 65 and 50","D":"Between 50 and 40","F":"Less than 40" }
    taken_policy=[]
    def find_cutoff(new):
        if len(new)==1:
            if new[0]==A[0]:
                taken_policy.append(policy[0])
                return policy_adopted["A"]
            elif new[0]==B[0]:
                taken_policy.append(policy[1])
                return policy_adopted["B"]
            elif new[0]==C[0]:
                taken_policy.append(policy[2])
                return policy_adopted["C"]
            elif new[0]==D[0]:
                taken_policy.append(policy[3])
                return policy_adopted["D"]
            elif new[0]==F[0]:
                taken_policy.append(policy[4])
                return policy_adopted["F"]
        elif len(new)==2:
            taken_policy.append(new[1])
            return new[1]
        elif len(new)>2:
            l=[]
            for j in range(1,len(new)-1):
                l.append(abs(new[j]-new[j+1]))
            m=max(l)
            ind=l.index(m)+1
            taken_policy.append((new[ind]+new[ind+1])/2)
            return (new[ind]+new[ind+1])/2
    new_policy=[find_cutoff(A),find_cutoff(B),find_cutoff(C),find_cutoff(D),find_cutoff(F)]
    cutoffpolicy.append(new_policy)

    for rollno, student in course["students"].items():
        total_marks = student["total_marks"]
        if total_marks >= taken_policy[0]:
            student["grade"] = "A"
        elif total_marks >= taken_policy[1]:
            student["grade"] = "B"
        elif total_marks >= taken_policy[2]:
            student["grade"] = "C"
        elif total_marks >= taken_policy[3]:
            student["grade"] = "D"
        else:
            student["grade"] = "F"
    # print(A,B,C,D,F,"this")        

def generate_summary(course):
    print("Course name:", course["cname"])
    print("Credits:", course["credits"])
    print("Assessments and their weights:", course["assessments"])
    print("Grading policy:", course["policy"])
    print()
    print("The Cutoffs of the grades are listed below : ")
    for i in cutoffpolicy:
        print("                                    Cutoff for 'A' Grade : ",i[0])
        print("                                    Cutoff for 'B' Grade : ",i[1])
        print("                                    Cutoff for 'C' Grade : ",i[2])
        print("                                    Cutoff for 'D' Grade : ",i[3])
        print("                                    Cutoff for 'F' Grade : ",i[4])
    print()
    cutoffpolicy.clear()
    grades = {}
    for student in course["students"].values():
        grade = student["grade"]
        if grade in grades:
            grades[grade] += 1
        else:
            grades[grade] = 1
    print("Grading summary:", grades)

def print_grades(course, grades_file):
    with open(grades_file, 'w') as f:
        f.write("The <Roll no.>, <Total Marks>, <Grades received> has been listed below.\n\n")
        for rollno, student in course["students"].items():
            f.write(f"{rollno} {student['total_marks']} {student['grade']}\n")
    f.close()        

def search_student(course, rollno):
    if rollno in course["students"]:
        student = course["students"][rollno]
        print("Roll no.:",rollno)
        print("Marks:", student["marks"])
        print("Total marks:", student["total_marks"])
        print("Grade:", student["grade"])
    else:
        print("Student not found")

if __name__ == "__main__":
    cname, credits = "IP", 4
    assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
    policy = [80, 65, 50, 40, 30]
    course = create_course(cname, credits, assessments, policy)
    # upload_marks(course, file_location)
    # do_grading(course)
    # # generate_summary(course)
    # for i in range(1200):
    #     search_student(course,2022047)
    # end_time=time.time()
    # print("Tolal time Elapsed is",end_time-start_time)
    while True:
        inp=int(input("Enter your choice ! what would you like to do ? "))
        if inp == 1:
            ce=input("Enter course name : ")
            cdt=int(input("Enter the total Credits of course : "))
            assessment =list(input("Enter the assessments as tuples Eg. ('labs', 30): ").split() ) #[("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
            policy_made=list(map(int,input("Enter policy made with space separated values : ").split()))
            course=create_course(ce, cdt, assessment, policy_made)
            print("course has been created successfully !")

        elif inp == 2:
            upload_marks(course, file_location)
            do_grading(course)
            print("Student data added successfully from the file!")
            print()
            print("Now what would you like to do ?")
            ta=["(1). Generate a summary","(2). Print the grades of all the students in the file","(3). Search for a student record by Roll no."]    
            for i in ta:
                print(i)

            new_inp=int(input("Now fill the new choice! :- "))
            if new_inp==1:
                print("Generating a summary !")
                print()
                generate_summary(course)
            elif new_inp==2:
                print("printing Grades of all the students in file location ",file_location)
                print()
                print_grades(course,grades_file)
            elif new_inp==3:
                inpt=int(input("Enter the Roll no. of the student :- "))
                print()
                search_student(course,inpt)

        elif inp == 3:
            print("You have exited successfully !")
            break
