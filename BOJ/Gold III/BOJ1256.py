#BOJ1256 사전 20210410
import sys
input = sys.stdin.readline

def main():
    n,m,k = map(int,input().rstrip().split())
    k -= 1
    dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for i in range(1,n+1): dp[i][0] = 1
    for i in range(1,m+1): dp[0][i] = 1
    for r in range(1,n+1):
        for c in range(1,m+1):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    if k+1 > dp[n][m]:
        print(-1)
    else:
        res = ""
        r,c = n,m
        while r != 0 or c != 0:
            if r == 0:
                res += "z"
                c -= 1
            elif c == 0:
                res += "a"
                r -= 1
            elif k < dp[r-1][c]:
                res += "a"
                r -= 1
            else:
                k -= dp[r-1][c]
                res += "z"
                c -= 1
        print(res)
if __name__ == '__main__':
    main()