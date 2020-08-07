#this is the recursive way to find the fibnacci series
#doing with recursive is not a good idea because it will take much much time.
#so better find any other efficient way.
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
input1=int(input())
for i in range(0, input1):
    print(fib(i))
