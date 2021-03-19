#BOJ1915 가장 큰 정사각형 20210319
import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split())
    li = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    dp = [[0 for _ in range(m)] for __ in range(n)]
    dr = [-1,0,-1]
    dc = [0,-1,-1]
    mx = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] == 0 : continue
            mn = 1001
            for k in range(3):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < n and 0 <= nc < m:
                    mn = min(mn, dp[nr][nc])
                else:
                    mn = 0
            dp[i][j] = mn + 1
            mx = max(dp[i][j], mx)
    print(mx**2)
if __name__ == '__main__':
    main()