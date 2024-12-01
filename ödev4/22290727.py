import sys
def merge(A,p,q,r):
    n1 = q-p+1 # sol yarının eleman sayısı
    n2 = r-q # sağ yarının eleman sayısı
    L = [0]*(n1+1) # sol yarı için boş liste
    R = [0]*(n2+1) # sağ yarı için boş liste
    for i in range(n1):
        L[i] = A[p+i] # sol yarının elemanları
    for j in range(n2):
        R[j] = A[q+j+1] # sağ yarının elemanları
    L[n1] = float('inf') # solun sonuncu sonsuz elemanı
    R[n2] = float('inf') # sağın sonuncu sonsuz elemanı
    i = j = 0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    return A

def merge_sort(A,p,r): # p: başlangıç, r: bitiş
    if p<r:
        q=(p+r)//2 # orta nokta
        merge_sort(A,p,q) # sol yarı
        merge_sort(A,q+1,r)  # sağ yarı
        merge(A,p,q,r)  # birleştirme işlemi
    return A

def partition(A,p,r):
    x = A[r] # pivot elemanı liste sonundan seçtim
    i = p-1 # i başlangıçta -1 pivotun solunda kaldıkça +1 olacak
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j] = A[j],A[i] #swap işlemi
    A[i+1],A[r] = A[r],A[i+1] # pivotu doğru yere koymam lazım i tane ondan küçük sayı varsa pivot i+1. eleman olmalı
    return i+1 # pivotun yeni yeri

def quick_sort(A,p,r): # p: başlangıç, r: bitiş
    if p<r:
        q=partition(A,p,r) # orta noktam
        quick_sort(A,p,q-1) # sol yarı
        quick_sort(A,q+1,r)  # sağ yarı
    return A

def partition_m(A,p,r):
    mean = sum(A[p:r+1])//len(A[p:r+1]) # pivot elemanı aritmetik ortalamadan seçtim
    diff = float('inf')
    pivot_index = p # pivotun indeksi başlangıçtan seçtim
    for i in range(p,r+1):
        if abs(mean-A[i])<diff:
            diff = abs(mean-A[i])
            pivot_index = i
    A[pivot_index], A[r] = A[r], A[pivot_index]  #pivotu sona taşıdım çünkü sonran sıralamalı algoritma yapıyorum
    x = A[r]  # pivot sondan seçildi
    i = p-1 # i başlangıçta -1 pivotun solunda kaldıkça +1 olacak
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j] = A[j],A[i] #swap işlemi
    A[i+1],A[r] = A[r],A[i+1] # pivotu doğru yere koymam lazım i tane ondan küçük sayı varsa pivot i+1. eleman olmalı
    return i+1 # pivotun yeni yeri

def quick_sort_m(A,p,r): # p: başlangıç, r: bitiş
    if p<r:
        q=partition_m(A,p,r) # orta noktam
        quick_sort_m(A,p,q-1) # sol yarı
        quick_sort_m(A,q+1,r)  # sağ yarı
    return A


choose = int(input())
input_lines = sys.stdin.read().strip().splitlines()
List = [int(line) for line in input_lines]

r = len(List)-1
p = 0

if choose == 0:
    Liste_sorted = merge_sort(List,p,r)
    print("MergeSort")

elif choose == 1:
    Liste_sorted = quick_sort(List,p,r)
    print("QuickSort")

elif choose == 2:
    Liste_sorted = quick_sort_m(List,p,r)
    print("QuickSort_M")

for i in range(p,r):
    print(List[i])
