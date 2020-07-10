# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refill, curr_refill, limit = 0,0,tank
    while limit < distance:  # While the destination cannot be reached with current fuel
        if curr_refill >= len(stops) or stops[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < len(stops)-1 and stops[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = stops[curr_refill] + tank  # Fill up the tank
        curr_refill += 1
    return num_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d=950
    # m=400
    # stops=[200,375,550,750]
    print(compute_min_refills(d, m, stops))
