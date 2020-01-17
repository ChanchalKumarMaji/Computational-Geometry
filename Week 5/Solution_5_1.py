# python3

def binary_search(X, val):
    l, h = 0, len(X)-1
    while l < h:
        mid = (l+h) // 2
        if X[mid] == val:
            return val
        if X[mid] < val:
            l = mid + 1
        else:
            h = mid
    if l > 0 and abs(X[l-1]-val) < abs(X[l]-val):
        return X[l-1]
    return X[l]

def solve(X, M):
    n, m = len(X), len(M)
    #print(X, M)
    X.sort()
    for i in range(m):
        print(binary_search(X, M[i]))


if __name__ == '__main__':
    n = int(input())
    X = [int(i) for i in input().split()]
    m = int(input())
    M = []
    for _ in range(m):
        M.append(int(input()))
    solve(X, M)
