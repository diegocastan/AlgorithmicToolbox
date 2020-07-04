# Uses python3
def calc_fib_table(n):
    if n<=1:
        return n
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2,len(fib)):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]

n = int(input())
print(calc_fib_table(n))
