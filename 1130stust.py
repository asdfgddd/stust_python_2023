
class Student:
    def __init__(self, school_name="南台科大", 
    department_name="資訊工程",
    department_head="徐鳳年", 
    student_name="王希民", 
    student_id="4g0b0019", 
    address="320桃園市中壢區龍川二街134號",
    credits=150, 
    gpa=3.19):
        self.school_name = school_name
        self.department_name = department_name
        self.department_head = department_head
        self.student_name = student_name
        self.student_id = student_id
        self.address = address
        self.credits = credits
        self.gpa = gpa

    def getSchoolName(self):
        return self.school_name

    def setSchoolName(self, school_name):
        self.school_name = school_name

    def getDepartmentName(self):
        return self.department_name

    def setDepartmentName(self, department_name):
        self.department_name = department_name

    def getDepartmentHead(self):
        return self.department_head

    def setDepartmentHead(self, department_head):
        self.department_head = department_head

    def getStudentName(self):
        return self.student_name

    def setStudentName(self, student_name):
        self.student_name = student_name

    def getStudentID(self):
        return self.student_id

    def setStudentID(self, student_id):
        self.student_id = student_id

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getCredits(self):
        return self.credits

    def setCredits(self, credits):
        self.credits = credits

    def getGPA(self):
        return self.gpa

    def setGPA(self, gpa):
        self.gpa = gpa
        
    def print_info(self):
        print("學校名稱:", self.school_name)
        print("系所名稱:", self.department_name)
        print("系主任:", self.department_head)
        print("學生姓名:", self.student_name)
        print("學號:", self.student_id)
        print("地址:", self.address)
        print("學分:", self.credits)
        print("平均成績:", self.gpa)
student = Student()
student.print_info()
 
student = Student()
student.print_info()
