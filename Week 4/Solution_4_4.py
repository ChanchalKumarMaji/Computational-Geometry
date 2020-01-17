# python3

def solve(n):
    # (n-2) th Catalan number
    n -= 2
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    print(dp[n])


if __name__ == '__main__':
    n = int(input())
    solve(n)
