# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    # Get the period
    period=2
    res = {}
    res[0] = 0
    res[1] = 1
    sum = 1
    while 1:
        previous, current = current % 10, (previous + current) % 10
        sum = (sum + current) % 10
        res[period] = sum
        period += 1
        if res[period-2] == 0 and sum == 1:
            break
    period -= 2

    # Get the res
    l = n % period
    return res[l]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = 100
    print(fibonacci_sum_naive(n))