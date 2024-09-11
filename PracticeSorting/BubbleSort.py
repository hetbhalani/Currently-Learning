a = [2,5,4,7,3,8,1]
n = len(a)

for i in range (0,n-1):
    for j in range (0,n-i-1):
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            
        
print(a)