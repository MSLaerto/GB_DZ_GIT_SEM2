print("Hell'no world")
print(2+2)

from random import randint
 
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
 
def bubbleSort(a):
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a                            
 
print(bubbleSort(a))