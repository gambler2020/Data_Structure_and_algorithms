import sys
def fib(n):
    if(n<=1):
        return n
    previous = 0
    current = 1
    for _ in range(n-2):
        previous, current = current, current + previous
    return current % 10
if __name__ == "__main__":
    input = sys.stdin.readline()
    n=int(input)
    print(fib(n))

