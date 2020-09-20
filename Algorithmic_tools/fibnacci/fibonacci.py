# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        return (calc_fib(n - 1) + calc_fib(n - 2)) #this prints next word

n = int(input())
for i in range(0, n+1):
    print(calc_fib(i), end="")
