N = int(input())
X = int(input())
handle = 0
for i in N:
    A = int(input())
    if X == A:
        handle=1

if handle == 1:
    print("YES")
else:
    print("NO")