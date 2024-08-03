class Employee:
    name = "Het"
    Langauge = "Python"

class inherit(Employee):
    salary = 123456789  

a = inherit()

print(a.salary, a.name)
