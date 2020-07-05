# Uses python3
import sys

def lcm_naive(a, b):
    ad, bd = max(a,b), min(a,b)
    while 1:
        ad, bd = bd, ad % bd
        if bd == 0:
            break
    gcd = ad
    return int(a*b/gcd)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # a, b = 28851538, 1183019
    print(lcm_naive(a, b))