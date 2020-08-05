#Given a sequence of non-negative integers a0,…,an−1, find the
#maximum pairwise product, that is, the largest integer that can
#be obtained by multiplying two different elements from the sequence
#(or, more formally, max0≤i≠j≤n−1aiaj). Different elements here mean
#ai and aj with i≠j (it can be the case that ai=aj).

#Input format

#    The first line of the input contains an integer n. The next line contains n non-negative integers a0,…,an−1 (separated by spaces).

#Constraints:

#    2≤n≤2⋅105; 0≤a0,…,an−1≤105.

#Output format:

#   Output a single number — the maximum pairwise product.

#input: 3
#       1 6 9

#Output: 54

def max_pair_product(n, l):
    index1=0
    index2=0
    for i in range(n):
        if l[i]>index1:
            index2=index1
            index1=l[i]
        elif l[i]>index2:
            index2=l[i]
    return index1*index2
n1=int(input())
l1=[int(k) for k in input().split()]
print(max_pair_product(n1, l1))
