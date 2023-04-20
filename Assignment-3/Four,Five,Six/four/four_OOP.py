import time
start_time=time.time()
task=["(1). creating a course","(2). adding Students marks for all assessments","(3). Exit."]
print("Choose an appropriate task no. to perform ... ")
for i in task:
    print(i)

filel=r"E:\IIITD Projects\IP\Project assignment - 3\Four,Five,Six\IPmarks.txt"
filep=r"E:\IIITD Projects\IP\Project assignment - 3\Four,Five,Six\four\output.txt"
# data={}
cutoffpolicy=[]
class courses:
    def __init__(self,cname, credits, assessments, policy):
        self.cname=cname
        self.credits=credits
        self.assessments=assessments
        self.policy=policy
        self.grade={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        self.studentdata={}
        # print(self.studentdata)

    def add_student(self,rollno,marks):
        self.studentdata[int(rollno)]=marks
        # print(self.studentdata)

    def do_grading(self):
            policy = self.policy
            print(policy)
            A=[]
            B=[]
            C=[]
            D=[]
            F=[]
            for rollno, marks in self.studentdata.items():
                total_marks = sum(marks.values())
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
            # print(taken_policy,new_policy)
            # print(A,B,C,D,F)
            grades = ['A', 'B', 'C', 'D', 'F']
            for rollno, marks in self.studentdata.items():
                total_marks = sum(marks.values())
                for i in range(len(taken_policy) - 1):
                    if total_marks >= taken_policy[i]:
                        self.studentdata[rollno]['grade'] = grades[i]
                        self.grade[grades[i]] += 1
                        break
            
    
    def give_summary(self):
        print("Course name : ",self.cname)
        print("Total Credits : ",self.credits)
        print("Assessments used for grading are: ")
        for i in self.assessments:
            print(i[0],":",i[1],"%") 
        print("Grading policy applied : ",self.policy)
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
        print("Providing the Grading summary : ")
        for i,j in self.grade.items():
            print(i,":",j)
        
    def print_grades(self, filep):
        with open(filep, 'w') as f:
            f.write("The <Roll no.>, <Total Marks>, <Grades received> has been listed below.\n\n")
            for rollno, marks in self.studentdata.items():
                k=[i for i in marks.values()]
                k.pop()
                total_marks=sum(k)
                f.write(f"{rollno}, {total_marks}, {marks['grade']}\n")
        f.close()

    def search_student(self, rollno):
        # print(self.studentdata)
        if rollno in self.studentdata:
            marks = self.studentdata[rollno]
            print("Roll no:", rollno)
            print("Marks:", marks)
            k=[i for i in marks.values()]
            k.pop()
            total_marks=sum(k)
            print("Total marks:", total_marks)
            print("Grade:", marks['grade'])
        else:
            print("Student not found")


def upload_marks(course,filel ):
    with open(filel, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            rollno = data[0]
            marks = {}
            for i in range(len(course.assessments)):
                marks[course.assessments[i][0]] = float(data[i + 1])
            courses.add_student(course,rollno, marks)
        # print(courses(studentdata))

cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40, 30]
course = courses(cname, credits, assessments,policy)
# upload_marks(course,filel)
# courses.do_grading(course)
# for i in range(1200):
#     end_time=time.time()
# print("Tolal time Elapsed is",end_time-start_time)
# courses.search_student(course,2022047)
# end_time=time.time()
# print("Tolal time Elapsed is",end_time-start_time)

# courses.add_student(course,rollno,marks)

while True:
    inp=int(input("Enter your choice ! what would you like to do ? "))
    # try:
    if inp == 1:
        ce=input("Enter course name : ")
        cdt=int(input("Enter the total Credits of course : "))
        assessment =list(input("Enter the assessments as tuples Eg. ('labs', 30),('midsem', 15): ").split() ) #[("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
        policy_made=list(map(int,input("Enter policy made with space separated values : ").split()))
        course = courses(ce, cdt, assessment,policy_made)
        print("course has been created successfully !")


    elif inp == 2:
        print()
        upload_marks(course,filel)
        courses.do_grading(course)
        # end_time=time.time()
        # print("Tolal time Elapsed is",end_time-start_time)
        print("Student data added successfully from the file!")
        print()
        print("Now what would you like to do ?")
        ta=["(1). Generate a summary","(2). Print the grades of all the students in the file","(3). Search for a student record by Roll no."]    
        for i in ta:
            print(i)
        new_inp=int(input("Now fill the new choice! :- "))
        if new_inp==1:
            print("Generating a summary !")
            courses.give_summary(course)

        elif new_inp==2:
            print("printing Grades of all the students in the file located at :",filep)
            courses.print_grades(course,filep)
        elif new_inp==3:
            roll=int(input("Enter the Roll no. of the student :- "))
            courses.search_student(course,roll)

    elif inp == 3:
        print("You have Exited from the program successfully !")
        break
    # except:
        # print("Please make a correct choice by choice number only ...")
