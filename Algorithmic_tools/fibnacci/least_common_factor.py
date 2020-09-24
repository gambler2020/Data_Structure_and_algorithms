def LCM(a, b):
    if a==0 or b==0:
        return "Undefined"
    for i in range(1, a*b + 1):
        if i%a==0 and i%b==0:
            return i
        
t=input()
m, n=map(int, t.split())
print(LCM(m, n))
