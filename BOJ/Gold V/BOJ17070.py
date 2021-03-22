#BOJ17070 파이프 옮기기1 20210322
import sys
input = sys.stdin.readline
GARO = 0
SERO = 1
DAEGAK = 2
def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp = [[[0] * 3 for _ in range(n)] for __ in range(n)]
    dp[0][1][GARO] = 1
    for c in range(2,n):
        if li[0][c] == 1: break
        dp[0][c][GARO] = 1
    for r in range(1,n):
        for c in range(2,n):
            if li[r][c] == 0 and li[r][c-1] == 0 and li[r-1][c] == 0:
                dp[r][c][DAEGAK] = sum(dp[r-1][c-1])
            if li[r][c] == 0:
                dp[r][c][GARO] = dp[r][c-1][GARO] + dp[r][c-1][DAEGAK]
                dp[r][c][SERO] = dp[r-1][c][SERO] + dp[r-1][c][DAEGAK]
    print(sum(dp[-1][-1]))
if __name__ == '__main__':
    main()