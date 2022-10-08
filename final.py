import random
class Student:
    def __init__(self, student_name,student_class,student_id):
        self.student_number = random.randint(10000,99999)
        self.student_name = student_name
        self.student_class = student_class
        self.student_id=random.randint(10000,99999)
        self.student_course= []
    def add_course(self,course):
        self.course = course
        self.student_course.append(course)

class Course:
    def __init__(self,course_name,course_class,course_id):
        self.course_name= course_name
        self.course_class = course_class
        self.course_id= course_id

def desplay_student_details(self):
    print("Course \t Name \t Class")
    print(self.student_course,"\t",self.student_name,"\t", self.student_class )



def find_course(course_name,courses):
    index = 0
    for i in courses:
        if i.course_name in course_name:
            return  index
        return -1
def find_student(student_number,student_name):
    index = 0
    for i in student_name:
        if i.student_number in student_name:
            return index
        index += 1
    return-1

course_list = []
student_list = []

while True:
    var = int(input("Select Choice Please \n"
                    "1. Add New Student \n" +
                    "2. Remove Student \n" +
                    "3. Edit Student \n" +
                    "4. Display All Students \n" +
                    "5. Create New Course \n" +
                    "6. Add course to student \n" +
                    "0. Exit \n"))

    if var ==0:
        exit()

    elif var==1:
        student_name = input("\n Enter Student Name")
        student_class = input("\n Enter Student Class (A-B-C)")
        while(True):
            if student_class in ["A","B","C"]:
                break
            else:
                student_class = input("Enter Student Class(A-B-C)")
                student = Student(student_name,student_class)
                student_list.append(student)
                print("Student Saved Successfully")

    elif var == 2:
        student_number = int(input("Enter Student Number"))
        search_result  = find_student(student_number, student_list)
        if search_result == -1:
            print("Student not exist")
        else:
            student_list[search_result].student_name = input("Enter Student Name")
            student_class = input("Select Student Class(A,B,C)")
            while True:
                if student_class in ("A","B","C"):
                    break
                else:
                    student_class = input("Select Student Class(A-B-C)")
                    student_list[search_result].student_class = student_class
                    print("Student information edited successful")
    elif var == 3:
        student_number = int(input("Enter Student Number"))
        search_result  = find_student(student_number,student_list)
        if search_result == -1:
            print("Student not exist")
        else:
            student_list.pop(search_result)
            print("Student reemoved Successful")
    elif var ==4:
        student_number = int(input("Enter Student Number"))
        search_result= find_student(student_number,student_list)
        student_list[search_result].desplay_student_details()

    elif var ==5:
        course_name = input("Enter Course Name")
        course_class  = input("Enter Course Class(A-B-C)")
        course = Course(course_name,course_class)
        print("Course Created Successful")

    elif var == 6:
        pass
    else:
        break









