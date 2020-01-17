# python3

import math

def area(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

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

def solve(m, M, P):
    n = len(P)
    zx, zy = (M[0]+M[2]+M[4])/3, (M[1]+M[3]+M[5])/3
    A = []
    for i in range(m):
        x, y = M[2*i], M[2*i+1]
        dy, dx = y-zy, x-zx
        A.append((math.atan2(dy, dx), i))
    A.sort()
    #print(A)
    for i in range(n):
        px, py = P[i]
        dy, dx = py-zy, px-zx
        a = math.atan2(dy, dx)
        v1 = binary_search(A, a)
        v0 = (v1-1) % m
        #print(v0, v1)
        a = area(M[2*v0], M[2*v0+1], M[2*v1], M[2*v1+1], px, py)
        if a == 0 and min(M[2*v0+1], M[2*v1+1]) <= py <= max(M[2*v0+1], M[2*v1+1]):
            print("BORDER")
        elif a > 0:
            print("INSIDE")
        else:
            print("OUTSIDE")


if __name__ == '__main__':
    m = int(input())
    M = [int(i) for i in input().split()]
    n = int(input())
    P = []
    for _ in range(n):
        px, py = map(int, input().split())
        P.append([px, py])
    solve(m, M, P)


# Good TestCase
# 5
# -2 -3 1 -4 3 -2 2 1 -2 1
# 2
# 3 -5
# 0 -5
