# python3

import math

def area(x1, y1, x2, y2, x3, y3):
    A = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if A > 0:
        return 1
    elif A < 0:
        return -1
    elif A == 0:
        return 0

def on_segment(x1, y1, x2, y2, x3, y3):
    if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        return True
    return False

def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # Intersection of the lines formed by segments [(x1, y1), (x2, y2)] and [(x3, y3), (x4, y4)]
    if x1 == x2:
        x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2 
    x = ((y1-y2)*(x3-x4)*x1 - (y3-y4)*(x1-x2)*x3 + (y3-y1)*(x1-x2)*(x3-x4)) / ((y1-y2)*(x3-x4) - (x1-x2)*(y3-y4))
    y = y1 + (y1-y2)*(x-x1) / (x1-x2)
    return (int(x), int(y))

def _solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    # Checking cases like
    # [(0, 0), (5, 5)] and [(5, 5), (7, 7)]
    # [(0, 0), (10, 0)] and [(10, 0), (9, 0)]
    p1, p2, p3, p4 = (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)
    if p1 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return (Ax, Ay)
    elif p1 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return (Ax, Ay)
    elif p2 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return (Bx, By)
    elif p2 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return (Bx, By)
    a1 = area(Ax, Ay, Bx, By, Cx, Cy)
    a2 = area(Ax, Ay, Bx, By, Dx, Dy)
    a3 = area(Cx, Cy, Dx, Dy, Ax, Ay)
    a4 = area(Cx, Cy, Dx, Dy, Bx, By)
    #print(a1, a2, a3, a4)
    if a1 != a2 and a3 != a4:
        x, y = intersection(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
        return (x, y)
    elif a1 == 0 and on_segment(Ax, Ay, Bx, By, Cx, Cy):
        return (Cx, Cy)
    elif a2 == 0 and on_segment(Ax, Ay, Bx, By, Dx, Dy):
        return (Dx, Dy)
    elif a3 == 0 and on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return (Ax, Ay)
    elif a4 == 0 and on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return (Bx, By)
    else:
        return False

def binary_search(A, a):
    #print(A, a)
    l, r = 0, len(A)-1
    while l < r:
        mid = (l+r) // 2
        if A[mid][0] == a:
            return A[mid][1]
        if A[mid][0] < a:
            l = mid + 1
        else:
            r = mid
    if r == len(A)-1 and A[r][0] < a:
        return A[0][1]
    return A[r][1]

def __solve(M, P):
    m, n = len(M), len(P)
    zx, zy = (M[0][0]+M[1][0]+M[2][0])/3, (M[0][1]+M[1][1]+M[2][1])/3
    A = []
    for i in range(m):
        x, y = M[i]
        dy, dx = y-zy, x-zx
        A.append((math.atan2(dy, dx), i))
    A.sort()
    #print(A)
    res = set()
    for i in range(n):
        px, py = P[i]
        dy, dx = py-zy, px-zx
        a = math.atan2(dy, dx)
        v1 = binary_search(A, a)
        v0 = (v1-1) % m
        #print(v0, v1)
        a = area(M[v0][0], M[v0][1], M[v1][0], M[v1][1], px, py)
        if a == 0 and min(M[v0][1], M[v1][1]) <= py <= max(M[v0][1], M[v1][1]):
            res.add((px, py))
        elif a > 0:
            res.add((px, py))
    return res

def solve(V, W):
    A = set()
    n, m = len(V), len(W)
    for i in range(n):
        Ax, Ay = V[i]
        Bx, By = V[(i+1)%n]
        for j in range(m):
            Cx, Cy = W[j]
            Dx, Dy = W[(j+1)%m]
            k = _solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
            if k != False:
                A.add(k)
    s1 = __solve(V, W)
    s2 = __solve(W, V)
    res = A.union(s1.union(s2))
    k = len(res)
    print(k)
    if k == 0:
        return
    M = list(res)
    zx, zy = (M[0][0]+M[1][0]+M[2][0])/3, (M[0][1]+M[1][1]+M[2][1])/3
    T = []
    for i in range(k):
        x, y = M[i]
        dy, dx = y-zy, x-zx
        T.append((math.atan2(dy, dx), str(x)+" "+str(y)))
    T.sort()
    print(" ".join([e[1] for e in T]))


if __name__ == '__main__':
    n = int(input())
    P = [int(i) for i in input().split()]
    V = [[P[2*i], P[2*i+1]] for i in range(n)]
    m = int(input())
    P = [int(i) for i in input().split()]
    W = [[P[2*i], P[2*i+1]] for i in range(m)]
    solve(V, W)
