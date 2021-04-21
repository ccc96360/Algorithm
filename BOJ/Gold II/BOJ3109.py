import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(r,c,li,visited,n,m):
    visited[r][c] = 1
    if c == m-1:
        return 1
    for dr in [-1,0,1]:
        nr = r + dr
        nc = c + 1
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and li[nr][nc] == '.':
            if dfs(nr,nc,li,visited,n,m) == 1:
                return 1
    return 0
def main():
    n,m = map(int,input().rstrip().split())
    li = [list(input().rstrip()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    res = 0
    for r in range(n):
        res += dfs(r,0,li,visited,n,m)
    print(res)
if __name__ == '__main__':
    main()