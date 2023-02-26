#Insertion sort harjutus
#Kasutatud allikad: Cormen T.H. Introduction to algorthms

A = [23,5,12,2,7,9,0,1,82,4,6,]

print(A)

for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i +1] = A[i]
        i -= 1
    A[i + 1] = key

print(A)