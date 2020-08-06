#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

#The first two terms are 0 and 1. All other terms are obtained by adding 
#the preceding two terms. This means to say the nth term is the sum of 
#(n-1)th and (n-2)th term. nth = (n-1)th + (n-2)th

n=int(input("How many fibonacci series want to print:"))
f=0
s=1
count=0
list1=[]
while count<n:
    list1.append(f)
    print(f) 
    next_num=s+f # calculate next number
    f=s #update first number to second number
    s=next_num #update second number to next_number
    count=count+1
print(list1)
