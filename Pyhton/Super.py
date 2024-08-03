class Employee:
    a = 1

    def __init__(self):
        print("Constructor of Employee")

class Coder(Employee):
    b = 2

    def __init__(self):
        super().__init__()
        print("Constructor of Coder")

class Manager(Coder):
    c = 3

    def __init__(self):
        super().__init__()
        print("Cunstructor of Manager")

one = Manager()
print(one.c, one.b, one.a)