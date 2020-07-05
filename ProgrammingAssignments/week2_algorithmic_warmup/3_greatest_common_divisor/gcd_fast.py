# Uses python3
import sys

def gcd_naive(a, b):

    a, b = max(a,b), min(a,b)
    while 1:
        a, b = b, a % b
        if b == 0:
            break
    return a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))