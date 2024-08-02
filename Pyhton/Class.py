class het:
    name = "Het"
    langauge= "Python"
    sem = 3

    def info(self):
        print(f"name is {self.name} and langauge known is {self.langauge}")

    @staticmethod
    def greet():
        print("Good morning")

obj = het()
obj.langauge = "Javascript"
obj.info()
obj.greet()