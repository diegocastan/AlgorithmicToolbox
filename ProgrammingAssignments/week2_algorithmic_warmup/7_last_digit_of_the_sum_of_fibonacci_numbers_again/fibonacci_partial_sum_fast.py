# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    n = to
    if n <= 1:
        return n

    previous = 0
    current  = 1

    # Get the period
    period=2
    res = []
    res.append(0)
    res.append(1)
    while 1:
        previous, current = current % 10, (previous + current) % 10
        res.append(current)
        period += 1
        if res[period-2] == 0 and current == 1:
            break
    period -= 2
    res.pop()
    res.pop()

    # Get the res
    l = n % period
    m = from_ % period
    if l == m:
        return res[l]
    else:
        if l > m:
            return sum(res[m:l+1])%10
        else:
            A = sum(res[m:])
            B = sum(res[:l+1])
            return (A+B)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #from_, to = 49,65
    print(fibonacci_partial_sum_naive(from_, to))