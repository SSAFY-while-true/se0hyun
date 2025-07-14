# BOJ 11758 CCW

p1X, p1Y = map(int, input().split())
p2X, p2Y = map(int, input().split())
p3X, p3Y = map(int, input().split())

if p1X == p2X:
    incline = 0
else:
    incline = (p2Y - p1Y) / (p2X - p1X)
var = p2Y - incline * p2X 

if p3Y == incline * p3X + var:
    print(0)
elif incline >= 0:
    if p3Y > incline * p3X + var:
        print(1)
    elif p3Y < incline * p3X + var:
        print(-1)
elif incline < 0:
    if p3Y > incline * p3X + var:
        print(-1)
    elif p3Y < incline * p3X + var:
        print(1)