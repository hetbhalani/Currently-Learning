# class het:
#     name = "Het"
#     langauge= "Python"
#     sem = 3

#     def __init__(self):
#         print("This is an object")

#     def info(self):
#         print(f"name is {self.name} and langauge known is {self.langauge}")

#     @staticmethod
#     def greet():
#         print("Good morning")

# obj = het()
# obj.langauge = "Javascript"
# print(obj.name, obj.langauge)

#######################################################

class program:
    compeny = "Microsoft"

    def __init__(self,name,langauge,salary):
         self.name = name
         self.langauge = langauge
         self.salary = salary

p = program("Het", "JavaScript", 1234567890)
print(p.name, p.langauge, p.salary)

#################################################################

class calc:
    def __init__(self, n):
        self.n = n
    
    def squre(self):
     print(f"Squre is {self.n * self.n}")

    def squreRoot(self):
     print(f"squreRoot is {self.n ** 1/2}")

    def cube(self):
     print(f"cube is {self.n * self.n * self.n}")

a = calc(4)
a.squre()
a.squreRoot()
a.cube()