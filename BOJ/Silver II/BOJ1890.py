#BOJ1890 점프 20210228
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    dx = [1,0]
    dy = [0,1]
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                print(dp[n-1][n-1])
                break
            for k in range(2):
                x = j + dx[k] * li[i][j]
                y = i + dy[k] * li[i][j]
                if 0 <= x < n and 0 <= y < n:
                    dp[y][x] += dp[i][j]
if __name__ == '__main__':
    main()