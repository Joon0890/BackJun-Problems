import sys 

dan = int(sys.stdin.read().splitlines()[0])

for i in range(1, 10):
    print(f"{dan} * {i} = {dan*i}")