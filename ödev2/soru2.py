length = int(input("Dizinin eleman sayısını girin: "))
elements = input("Dizinin elemanlarını girin: ").split(", ")

i = 0 #index

while i < length:    
    startFromThis = [elements[i]]
    i += 1
    
    # ilk elemandan küçükse buradaki listeye eklemeye devam et 
    while i < length and elements[i] < startFromThis[-1]:
        startFromThis.append(elements[i])
        i += 1
    
    # o satırı bas, listede birden fazla eleman varsa , ekle
    print(", ".join(map(str, startFromThis)))
