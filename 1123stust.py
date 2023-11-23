

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount
        return self.emp_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

adams = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
jones = Employee("E7499", "JONES", 45000, "RESEARCH")
martin = Employee("E7900", "MARTIN", 50000, "SALES")
smith = Employee("E7698", "SMITH", 55000, "OPERATIONS")


adams.emp_assign_department("SALES")
adams.print_employee_details()
print(f"New Salary after overtime: {adams.calculate_emp_salary(60)}")





#class Car:
    #def __init__(self, brand, model, year, mileage, price,place):
        #self.brand = brand
        #self.model = model
        #self.year = year
        #self.mileage = mileage
        #self.price = price
        #self.place = place

#porsche_718 = Car('保時捷', '718', 2017, '600,000', '250,000','台南市永康區南台街道')



#print(f"品牌: {porsche_718.brand}")
#print(f"車款: {porsche_718.model}")
#print(f"年份: {porsche_718.year}")
#print(f"里程: {porsche_718.mileage}")
#print(f"價格: {porsche_718.price}台幣")
#print(f"地點: {porsche_718.place}")

