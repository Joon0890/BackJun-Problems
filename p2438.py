import sys 

data = sys.stdin.read().splitlines()
line_num = int(data[0])

for i in range(line_num):
    for j in range(i+1):
        print("*", end="")
    print()