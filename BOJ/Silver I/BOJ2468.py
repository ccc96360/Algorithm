#BOJ2468 안전 영역 20210307
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(p, safe,n,li,visited):
    global dx,dy
    x = p[0]
    y = p[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if li[ny][nx] > safe and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs((nx,ny), safe, n, li, visited)

def main():
    n = int(input())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    max_ = 1
    for safe in range(1,101):
        visited = [[False for _ in range(n)] for __ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and li[i][j] > safe:
                    visited[i][j] = True
                    dfs((j,i), safe, n, li, visited)
                    cnt += 1
        max_ = max(cnt, max_)
    print(max_)

if __name__ == '__main__':
    main()