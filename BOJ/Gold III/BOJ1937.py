#BOJ1937 욕심쟁이 판타 20210403
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]

dp = [] #(r,c)로 부터 몇 일 생존 가능한가
li = []

def dfs(r,c,n):
    global dp
    mx = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and li[nr][nc] > li[r][c]:
            if dp[nr][nc] != 0:
                mx = max(mx, dp[nr][nc])
            else:
                mx = max(mx,dfs(nr,nc,n))
    dp[r][c] = mx + 1
    return dp[r][c]
def main():
    global li,dp
    n = int(input())
    dp = [[0 for _ in range(n)] for __ in range(n)]
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if dp[r][c] != 0: continue
            dfs(r,c,n)
    res = 0
    for v in dp:
        res = max(max(v),res)
    print(res)
if __name__ == '__main__':
    main()