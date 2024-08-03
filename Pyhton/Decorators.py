#class method

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(cls.a)

obj = Employee()
obj.a = 123

obj.show()