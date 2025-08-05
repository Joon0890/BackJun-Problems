import sys
data = list(map(int, sys.stdin.read().splitlines()))

line1 = data[0] * (data[1] % 10)
line2 = data[0] * (data[1] % 100 // 10)
line3 = data[0] * (data[1] // 100)

print(line1)
print(line2)
print(line3)
print(line1 + line2 * 10 + line3 * 100)