n = int(input())
list1 = []

for i in range(0,n+1):
    list1.append(0)

counter = 1
for i in range(0,n+1):
    for j in range(0,n+1,counter):
        if list1[j] == 1:
            list1[j] = 0
        else:
            list1[j] = 1
    counter += 1
for i in range(0,n+1):
    if (list1[i]==1):
        print(i)
