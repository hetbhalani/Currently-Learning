list = [2,5,4,7,1,6,9]
n = len(list)

for i in range (0,n-1):
    min = i
    for j  in range (i+1,n):
        if(list[j] < list[min]):
            min = j
    list[i], list[min] =  list[min], list[i]

print(list)