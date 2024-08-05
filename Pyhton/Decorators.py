#class method

class Employee:
    # a = 1
    # @a.setter
    # def a(self,val):

    @property
    def a(self):
        return self.obj
    # @classmethod
    # def show(cls):
    #     print(cls.a)

obj = Employee()
obj.a = 10
print(obj.a)
