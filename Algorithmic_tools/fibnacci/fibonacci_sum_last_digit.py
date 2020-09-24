# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 0

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += previous%10

    return sum

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_naive(n))
