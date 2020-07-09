# Uses python3
import sys

def get_change(m):

    # First 10 coins
    nt = m // 10
    mres = m % 10

    # Then the 5 coins
    nf = mres // 5
    mres = mres % 5

    # Finally 1 coins
    no = mres

    return nt+nf+no

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 15
    print(get_change(m))
