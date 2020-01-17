# python3

def solve(n, V):
    last, temp = 0, 0
    for i in range(n):
        x1, y1, x2, y2, x3, y3 = V[2*((i-1)%n)], V[2*((i-1)%n)+1], V[2*i], V[2*i+1], V[2*((i+1)%n)], V[2*((i+1)%n)+1]
        v1_x, v1_y = x1-x2, y1-y2
        v2_x, v2_y = x3-x2, y3-y2
        temp = v1_x*v2_y - v1_y*v2_x
        if temp != 0:
            if last * temp < 0:
                return "NOT_CONVEX"
            last = temp    
    return "CONVEX"


if __name__ == '__main__':
    n = int(input())
    V = [int(i) for i in input().split()]
    print(solve(n, V))
