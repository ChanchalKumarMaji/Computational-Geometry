# python3

def anticlockwise_area(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def solve(Ax, Ay, Bx, By, P):
    n = len(P)
    for i in range(n):
        px, py = P[i]
        area = anticlockwise_area(Ax, Ay, Bx, By, px, py)
        if area > 0:
            print("LEFT")
        elif area < 0:
            print("RIGHT")
        elif area == 0:
            if min(Ax, Bx) <= px <= max(Ax, Bx) and min(Ay, By) <= py <= max(Ay, By):
                print("ON_SEGMENT")
            else:
                print("ON_LINE")


if __name__ == '__main__':
    Ax, Ay, Bx, By = map(int, input().split())
    P = []
    n = int(input())
    for _ in range(n):
        px, py = map(int, input().split())
        P.append([px, py])
    solve(Ax, Ay, Bx, By, P)
