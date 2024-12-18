class Student:
    def __init__(self,name: str ,age: int):
        #Validation
        assert age >= 18, "you are underaged"
        
        
        self.name = name
        self.age = age
        
        print(f"Hi I'm {name}")
        print(age)
        
    def dblAge(self):
        return self.age*2
        
    
s1 = Student("Het",18)
# s1.name = "Het"
# s1.age = 18

s2 = Student("Bhai",12)
# s2.name = "Bhai"
# s2.age = 1234

print(s1.dblAge())