class Student:
    def __init__(self, name, id, department, elective):
        self.name = name
        self.id = id
        self.department = department
        self.elective = elective

    def display(self):
        print(f"姓名: {self.name}")
        print(f"學號: {self.id}")
        print(f"科系: {self.department}")
        print(f"選修課程: {self.elective}")

# 初始化學生資訊
st1 = Student("徐鳳年", "4b0g0021", "資訊工程", "健康教育")
st2 = Student("王熹民", "400024", "電機系", "防止自殺")
st3 = Student("北口", "400094", "生化系", "人生哲學")

# 儲存所有學生的資訊
students = [st1, st2, st3]

# 查詢學生的科系和選修課程
def query(id):
    for student in students:
        if student.id == id:
            student.display()
            break

# 單獨查詢學生科系並顯示選修科系
query("4b0g0021")
