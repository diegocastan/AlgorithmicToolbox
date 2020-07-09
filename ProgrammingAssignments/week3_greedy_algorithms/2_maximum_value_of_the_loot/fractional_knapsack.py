# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    vpu = [values[i]/weights[i] for i in range(len(values))]
    tp = 0
    value = 0

    while tp < capacity:
        tm = max(vpu)
        wh = vpu.index(tm)
        if weights[wh] == 0:
            vpu.pop(wh)
            weights.pop(wh)
            if not weights:
                break
            continue
        else:
            if capacity - tp >= weights[wh]:
                tp += weights[wh]
                value += tm * weights[wh]
                weights[wh] = 0
            else:
                portion = capacity - tp
                tp += portion
                value += tm * portion
                weights[wh] -= portion


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # n, capacity = 1,1000
    # values = [500]
    # weights = [30]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
