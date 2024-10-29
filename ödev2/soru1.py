num1 = int(input("İlk sayı: "))
num2 = int(input("İkinci sayı: "))
ebob = 1
while (num1 !=0  and num2 !=0): 
    if num1%2==0 and num2%2==0: #ikisi de çift sayı
      num1 = num1/2
      num2 = num2/2
      ebob *= 2
    elif num1%2==0 and num2%2!=0:
       num1 =  num1/2
    elif num1%2!=0 and num2%2==0:
       num2 = num2/2
    elif num1%2!=0 and num2%2!=0:  #ikisi de tek sayı
        if num1 >= num2:       
            num1 = num1-num2
        else:
            num2 = num2-num1
    
if num1 == 0:
   ebob*=num2
else:
   ebob*=num1

ebob = int(ebob)
print(ebob)
