n = int(input("Enter n:"))
while (n<1):
    n = int(input("Enter n again(n>0): "))

elements = []
for i in range(n):
    elements.append(int(input()))
    
for i in range(n):
    result = 1
    for j in range(n):
        if i !=  j:            
            result *= elements[j]
    print(result)