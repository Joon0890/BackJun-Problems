import sys
data = sys.stdin.read().splitlines()

for i in range(1, int(data[0]) + 1):
    nums = list(map(int, data[i].split(" ")))
    print(nums[0] + nums[1])