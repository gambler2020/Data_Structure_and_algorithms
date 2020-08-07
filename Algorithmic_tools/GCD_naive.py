#This is the way of finding GCD(greatest common divisor) using Naive algorithm
#but this is not a good idea to go with Naive because consuming lots of time.
# so better is find another efficient way to get it within a small number of time

def GCD(a, b):
    if a>b:
        for i in range(a, 1, -1):
            if a%i==0 and b%i==0:
                return i
            else:
                continue
    else:
        for i in range(b, 1, -1):
            if a%i==0 and b%i==0:
                return i
            else:
                continue
print(GCD(11178992, 25536788))
