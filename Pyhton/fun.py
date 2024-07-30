def abc(n):
    if(n == 1 or n == 0):
        return 1
    return n * abc(n-1)

print(abc(5)) 
