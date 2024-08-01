# f = open("testFile.txt")
# data = f.read()
# print(data)
# f.close()

# s = "i am Het Bhalani"
# f = open("testFile.txt", "w")
# f.write(s)
# f.close()

f = open("testFile.txt")
lines = f.readlines()
print(lines)
f.close()

with open ("testFile.txt") as f:
    print(f.read()) 