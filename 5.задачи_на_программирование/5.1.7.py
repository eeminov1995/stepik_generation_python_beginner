# Ход коня

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x2 - x1) * (y2 - y1) == 2 or (x2 - x1) * (y2 - y1) == -2:
    print("YES")
else:
    print("NO")