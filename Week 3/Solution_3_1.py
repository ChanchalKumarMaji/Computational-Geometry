# python3

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
    x = ((y1-y2)*(x3-x4)*x1 - (y3-y4)*(x1-x2)*x3 + (y3-y1)*(x1-x2)*(x3-x4)) / ((y1-y2)*(x3-x4) - (x1-x2)*(y3-y4))
    y = y1 + (y1-y2)*(x-x1) / (x1-x2)
    return (int(x), int(y))

def _solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    # Checking cases like
    # [(0, 0), (5, 5)] and [(5, 5), (7, 7)]
    # [(0, 0), (10, 0)] and [(10, 0), (9, 0)]
    p1, p2, p3, p4 = (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)
    if p1 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return "The intersection point is ({}, {}).".format(Ax, Ay)
    elif p1 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return "The intersection point is ({}, {}).".format(Ax, Ay)
    elif p2 == p3 and not on_segment(Ax, Ay, Bx, By, Dx, Dy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return "The intersection point is ({}, {}).".format(Bx, By)
    elif p2 == p4 and not on_segment(Ax, Ay, Bx, By, Cx, Cy) and not on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return "The intersection point is ({}, {}).".format(Bx, By)
    a1 = area(Ax, Ay, Bx, By, Cx, Cy)
    a2 = area(Ax, Ay, Bx, By, Dx, Dy)
    a3 = area(Cx, Cy, Dx, Dy, Ax, Ay)
    a4 = area(Cx, Cy, Dx, Dy, Bx, By)
    #print(a1, a2, a3, a4)
    if a1 != a2 and a3 != a4:
        x, y = intersection(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
        return "The intersection point is ({}, {}).".format(x, y)
    elif a1 == 0 and on_segment(Ax, Ay, Bx, By, Cx, Cy):
        return "A common segment of non-zero length."
    elif a2 == 0 and on_segment(Ax, Ay, Bx, By, Dx, Dy):
        return "A common segment of non-zero length."
    elif a3 == 0 and on_segment(Cx, Cy, Dx, Dy, Ax, Ay):
        return "A common segment of non-zero length."
    elif a4 == 0 and on_segment(Cx, Cy, Dx, Dy, Bx, By):
        return "A common segment of non-zero length."
    else:
        return "No common points."

def solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    print(_solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy))


if __name__ == '__main__':
    Ax, Ay, Bx, By = map(int, input().split())
    Cx, Cy, Dx, Dy = map(int, input().split())
    solve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
