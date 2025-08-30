import sys

data = sys.stdin.read().splitlines()
num = int(data[0])
sum = 0

for i in range(1, num+1):
    sum += i

print(sum)