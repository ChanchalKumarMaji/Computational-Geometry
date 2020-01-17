# python3

def area(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def _solve(m, M, px, py):
    intersections = 0
    for j in range(m):
        Ax, Ay, Bx, By = M[2*((j-1)%m)], M[2*((j-1)%m)+1], M[2*j], M[2*j+1]
        a = area(Ax, Ay, Bx, By, px, py)
        if a == 0 and min(Ay, By) <= py <= max(Ay, By):
            return "BORDER"
        elif min(Ay, By) <= py < max(Ay, By):
            if Ay != By:
                x = Ax + (Ax-Bx)*(py-Ay) / (Ay-By)
                if x <= px:
                    intersections += 1
    if intersections % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"

def solve(m, M, P):
    for i in range(n):
        px, py = P[i]
        print(_solve(m, M, px, py))


if __name__ == '__main__':
    m = int(input())
    M = [int(i) for i in input().split()]
    n = int(input())
    P = []
    for _ in range(n):
        px, py = map(int, input().split())
        P.append([px, py])
    solve(m, M, P)
