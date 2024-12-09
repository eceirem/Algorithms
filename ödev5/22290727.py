n = int(input()) #n elemanlı bir dizi
A = [0]*n #0'a atanmış dizi
k = 0 #istenen counter
for i in range(n): #n^2 karmaşıklıkta bir döngü ile çözüyorum
    for j in range(i,n): #i'den n'ye gitsin ki 
                       #eski i<jler sağlansın 
                       #yoksa 3 3 3 gibi bir çıktı elde ederiz

        if A[i] < A[j]: #A[i] < A[j] kontrolü
            A[i]+=1
            k+=1
        else: #A[i] > A[j] kontrolü
            A[j]+=1 
            k+=1
        print(A) #A'yı yazdır
print(k) #k'yi yazdır        
            