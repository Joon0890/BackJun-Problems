import sys
point = int(sys.stdin.read().splitlines()[0])

if point <= 100 and point >= 90:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")