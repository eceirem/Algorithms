n = int(input("Enter n:"))
while (n<1):
    n = int(input("Enter n again(n>0): "))

elements = []
for i in range(n):
    elements.append(int(input("Enter element:")))

right = [1]*n
for i in range(n-2, -1, -1):  #sağdan sola
    right[i] = right[i+1] * elements[i+1]

left = [1]*n
for j in range(1,n): #soldan sağa gidiyoruz en sol her zaman 1
    left[j] = left[j-1] * elements[j-1]

for k in range(n):
    result = left[k]*right[k]
    print(result)
    