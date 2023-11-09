
def demo(name, age):
    
    print(name, age)

demo("Ben", 25)
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)



def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")
                    
def outer_fun(a, b):
    square = a ** 2

   
    def addition(a, b):
        return a + b

    
    add = addition(a, b)
    
    return add + 5

result = outer_fun(5, 10)
print(result)


def addition(num):
    if num:
        
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)



def display_student(name, age):
    print(name, age)


display_student("Emma", 26)


showStudent = display_student

showStudent("Emma", 26)



print(list(range(4, 30, 2)))


x = [4, 6, 8, 24, 12, 2]
print(max(x))