# python3

import math

def area(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def solve(n, P):
    min_y_max_x = 0
    for i in range(1, n):
        px, py = P[2*i], P[2*i+1]
        if py < P[2*min_y_max_x+1] or (py == P[2*min_y_max_x+1] and px > P[2*min_y_max_x]):
            min_y_max_x = i
    #print(min_y_max_x)
    pivot_x, pivot_y = P[2*min_y_max_x], P[2*min_y_max_x+1]
    A = []
    for i in range(n):
        if i != min_y_max_x:
            px, py = P[2*i], P[2*i+1]
            dx, dy = px-pivot_x, py-pivot_y
            A.append((math.atan2(dy, dx), i))
    A.sort()
    #print(A)
    A = [e[1] for e in A]
    stack = [A[-1], min_y_max_x]
    i = 0
    while i < len(A):
        prev, top = stack[-2], stack[-1]
        new = A[i]
        if area(P[2*prev], P[2*prev+1], P[2*top], P[2*top+1], P[2*new], P[2*new+1]) > 0:
            stack.append(new)
            i += 1
        else:
            _ = stack.pop()
    #print(stack)
    res = stack[:-1]
    #remove collinear points that may have been initially selected
    p1, p2, p3 = res[-1], res[0], res[1]
    if area(P[2*p1], P[2*p1+1], P[2*p2], P[2*p2+1], P[2*p3], P[2*p3+1]) == 0:
        res = res[1:]
    print(len(res))
    print(" ".join([str(P[2*i])+" "+str(P[2*i+1]) for i in res]))


if __name__ == '__main__':
    n = int(input())
    P = [int(i) for i in input().split()]
    solve(n, P)


#15
#-10 -2 -7 2 -4 3 -6 5 -8 7 -2 8 2 3 4 5 6 1 7 -5 2 -7 -4 4 -8 -6 -7 1 2 5

