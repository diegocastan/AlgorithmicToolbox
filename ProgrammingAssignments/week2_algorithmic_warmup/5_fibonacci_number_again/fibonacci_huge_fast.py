# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    # Get the period
    period=2
    res = {}
    res[0] = 0
    res[1] = 1
    while 1:
        previous, current = current, (previous + current) % m
        res[period] = current
        period += 1
        if previous == 0 and current == 1:
            break
    period -= 2

    # Get the res
    l = n % period
    return res[l]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # n, m = 10, 2
    print(get_fibonacci_huge_naive(n, m))