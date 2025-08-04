import sys
data = sys.stdin.read().split(" ")
A, B = int(data[0]), int(data[1])

if A > B:
    print(">")
elif A == B:
    print("==")
else:
    print("<")