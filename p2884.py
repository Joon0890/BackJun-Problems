import sys

data = sys.stdin.read().split(' ')

H, M = data[0], data[1]

H = int(H)
M = int(M)

total = H * 60 + M
new_time = total - 45

if new_time < 0:
    new_time += 24 * 60

new_H = new_time // 60
new_M = new_time % 60

print(new_H, new_M)