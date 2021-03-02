#BOJ1932 정수 삼각형 20210302
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp = [[0 for _ in range(i+1)] for i in range(n)]
    dp[0][0] = li[0][0]
    for i in range(1,n):
        for j in range(i+1):
            dp[i][j] = li[i][j]
            if 0 < j < i:
                dp[i][j] += max(dp[i-1][j],dp[i-1][j-1])
            else:
                dp[i][j] += dp[i-1][j] if j == 0 else dp[i-1][j-1]
    print(max(dp[-1]))
if __name__ == '__main__':
    main()