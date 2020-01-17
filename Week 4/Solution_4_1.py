# python3

from itertools import combinations

def area(x1, y1, x2, y2, x3, y3):
    A = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if A > 0:
        return 1
    if A < 0:
        return -1
    if A == 0:
        return 0

def on_segment(x1, y1, x2, y2, x3, y3):
    if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        return True
    return False

def intersects(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    # Checking cases like
    # [(0, 0), (5, 5)] and [(5, 5), (7, 7)]
    # [(0, 0), (10, 0)] and [(10, 0), (9, 0)]
    p1, p2, p3, p4 = (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)
    if p1 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return False
    elif p1 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return False
    elif p2 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return False
    elif p2 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return False
    a1 = area(Ax, Ay, Bx, By, Cx, Cy)
    a2 = area(Ax, Ay, Bx, By, Dx, Dy)
    a3 = area(Cx, Cy, Dx, Dy, Ax, Ay)
    a4 = area(Cx, Cy, Dx, Dy, Bx, By)
    if a1 != a2 and a3 != a4:
        if p1 == p3 or p1 == p4:
            return False
        if p2 == p3 or p2 == p4:
            return False
        return True
    elif a1 == 0 and on_segment(Ax, Ay, Bx, By, Cx, Cy):
        return True
    elif a2 == 0 and on_segment(Ax, Ay, Bx, By, Dx, Dy):
        return True
    elif a3 == 0 and on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return True
    elif a4 == 0 and on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return True
    else:
        return False

def inside_polygon(V, px, py):
    m = len(V)
    intersections = 0
    for j in range(m):
        Ax, Ay = V[(j-1)%m]
        Bx, By = V[j]
        if min(Ay, By) <= py < max(Ay, By):
            if Ay != By:
                x = Ax + (Ax-Bx)*(py-Ay) / (Ay-By)
                if x <= px:
                    intersections += 1
    return intersections % 2 == 1

def is_internal(p1, p2, V):
    x1, y1 = V[p1]
    x2, y2 = V[p2]
    x, y = (x1+x2)/2, (y1+y2)/2
    return inside_polygon(V, x, y)

def decide(p1, p2, V):
    n = len(V)
    Ax, Ay = V[p1]
    Bx, By = V[p2]
    for i in range(n):
        Cx, Cy = V[i]
        Dx, Dy = V[(i+1)%n]
        if intersects(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
            return " ".join(map(str, [Ax, Ay, Bx, By])) + " " + "INTERSECT"
    if is_internal(p1, p2, V):
        return " ".join(map(str, [Ax, Ay, Bx, By])) + " " + "INTERNAL"
    return " ".join(map(str, [Ax, Ay, Bx, By])) + " " + "EXTERNAL"

def solve(V):
    n = len(V)
    print(n*(n-1)//2 - n)
    for seg in list(combinations(list(range(n)), 2)):
        p1, p2 = seg
        if not(abs(p1-p2) == 1 or abs(p1-p2) == n-1):
            print(decide(p1, p2, V))


if __name__ == '__main__':
    n = int(input())
    P = [int(i) for i in input().split()]
    V = [[P[2*i], P[2*i+1]] for i in range(n)]
    solve(V)
