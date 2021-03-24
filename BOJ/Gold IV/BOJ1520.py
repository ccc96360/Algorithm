#BOJ1520 내리막길 20210324
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

li = []
dp = []
dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = set()
def dfs(p,n,m):
    r,c = p
    if r == n-1 and c == m-1: return 1
    if dp[r][c] != 0 or (r,c) in visited: return dp[r][c]
    visited.add((r,c))
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if li[r][c] > li[nr][nc]:
                dp[r][c] += dfs((nr,nc), n, m)
    return dp[r][c]
def main():
    global li,dp
    n,m = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp = [[0 for __ in range(m)]for _ in range(n)]
    dfs((0,0), n, m)
    print(dp[0][0])
if __name__ == '__main__':
    main()