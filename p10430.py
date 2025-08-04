import sys 
data = sys.stdin.read().split(" ")

A, B, C = int(data[0]), int(data[1]), int(data[2])

print((A + B) % C)
print(((A % C) + (B % C)) %C ) 
print((A * B) % C)
print(((A % C) * (B % C)) %C )