# python3

def area(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) > 0

def _solve(m, V, px, py):
    resR = []
    resL = []
    for i in range(m):
        prev_x, prev_y = V[2*((i-1)%m)], V[2*((i-1)%m)+1]
        cur_x, cur_y = V[2*i], V[2*i+1]
        next_x, next_y = V[2*((i+1)%m)], V[2*((i+1)%m)+1]
        e_prev = area(prev_x, prev_y, cur_x, cur_y, px, py)
        e_next = area(cur_x, cur_y, next_x, next_y, px, py)
        if not e_prev and e_next:
            resR.append(cur_x)
            resR.append(cur_y)
        if e_prev and not e_next:
            resL.append(cur_x)
            resL.append(cur_y)
    return " ".join(map(str, resL+resR))

def solve(m, V, P):
    n = len(P)
    for i in range(n):
        px, py = P[i]
        print(_solve(m, V, px, py))


if __name__ == '__main__':
    m = int(input())
    V = [int(i) for i in input().split()]
    n = int(input())
    P = []
    for _ in range(n):
        px, py = map(int, input().split())
        P.append([px, py])
    solve(m, V, P)
