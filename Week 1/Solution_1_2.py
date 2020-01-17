# python3

def area(x1, y1, x2, y2, x3, y3):
    return abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))

def solve(Ax, Ay, Bx, By, Cx, Cy, P):
    n = len(P)
    for i in range(n):
        px, py = P[i]
        a1 = area(Ax, Ay, Bx, By, px, py)
        a2 = area(Bx, By, Cx, Cy, px, py)
        a3 = area(Cx, Cy, Ax, Ay, px, py)
        a = area(Ax, Ay, Bx, By, Cx, Cy)
        if a1 + a2 + a3 == a:
            if a1 == 0 or a2 == 0 or a3 == 0:
                print("BORDER")
            else:
                print("INSIDE")
        else:
            print("OUTSIDE")


if __name__ == '__main__':
    Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
    n = int(input())
    P = []
    for _ in range(n):
        px, py = map(int, input().split())
        P.append([px, py])
    solve(Ax, Ay, Bx, By, Cx, Cy, P)
