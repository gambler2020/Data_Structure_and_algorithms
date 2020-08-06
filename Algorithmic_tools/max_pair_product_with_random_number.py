#find maximum product from random generated array.
import random
def max_prod_pair(n, a):
    max1=0
    max2=0
    for i in range(0, n):
        if a[i]>max1:
            max2=max1
            max1=a[i]
        elif a[i]>max2:
            max2=a[i]
    return max1*max2
n1=int(input("How many random number want to generate:"))
list1=[]
for j in range(0, n1):
    n=int(random.randint(0,20))
    list1.append(n)
print("Random generated List:",list1)
print("Maximum product pair is:",max_prod_pair(n1, list1))
