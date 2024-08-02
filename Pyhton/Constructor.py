class het:
    name = "Het"
    langauge= "Python"
    sem = 3

    def __init__(self):
        print("This is an object")

    def info(self):
        print(f"name is {self.name} and langauge known is {self.langauge}")

    @staticmethod
    def greet():
        print("Good morning")

obj = het()
obj.langauge = "Javascript"
print(obj.name, obj.langauge)