#Walrus

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

#type defination

n: int = 5

def greet(name: str) -> str:
    return f"Hi {name}"

print(greet("Het"))