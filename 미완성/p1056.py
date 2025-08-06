import sys 
import math

data = sys.stdin.read().splitlines()
N = int(data[0])

if not (N > 0 and N < 10**18):
    ValueError("숫자 범위 오류")

def S1():
    min = 2 + abs(N - 2 ** round(math.log(N, 2)))

    prime = 3
    while prime <= N:
        x = round(math.log(N, prime))
        diff = abs(N - prime ** x)
        if min >= prime + diff:
            min = prime + diff
        print(prime, x, diff, min)
        prime += 1

    return min

times = S1()
print(times)

    



    


