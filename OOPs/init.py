class Student:
    dis_fees = 0.8 #20% discount on fees 
    def __init__(self,name: str ,age: int, fees: int):
        #Validation
        assert age >= 18, "you are underaged"
                
        self.name = name
        self.age = age
        self.fees = fees
        
        print(f"Hi I'm {name}")
        # print(f'i am {age} years old')
        # print(f"i paid {fees} rupees")
        
    def dblAge(self):
        return self.age*2
        
    def applyDis(self):
        self.fees = self.fees * Student.dis_fees
    
s1 = Student("Het",19,120000)
# s1.name = "Het"
# s1.age = 18

s2 = Student("Bhai",20,50000)
# s2.name = "Bhai"
# s2.age = 1234

# print(s1.dblAge())

# print(Student.__dict__) #print all class level attribute
# print(s1.__dict__) #print all instence level attribute
s1.applyDis()
s2.applyDis()
print(s1.fees)
print(s2.fees)

s2.dis_fees = 0.7
s2.applyDis()
print(s2.fees)