#BOJ2225 합분해 20210317
import sys
input = sys.stdin.readline

def main():
    n,k = map(int, input().rstrip().split())
    dp = [[0] * (n+1)] + [ [1 for __ in range(n+1)] for _ in range(k)]
    for i in range(2,k+1):
        for j in range(1,n+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
    print(dp[k][n])
if __name__ == '__main__':
    main()