#import sys
def fib(n):
    if(n<=1):
        return n
    previous = 0
    current = 1
    a=[]
    for _ in range(n):
        a.append(previous)
        previous, current = current, current + previous
    #return current % 10
    return a
#if __name__ == '__main__':
#    input = sys.stdin.read()
n=int(input())
print(fib(n))
