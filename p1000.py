import sys
data = sys.stdin.read().split(" ")
if not(int(data[0]) > 0):
    ValueError
if not(int(data[1]) < 10):
    ValueError
print(int(data[0])+int(data[1]))
