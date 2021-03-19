#BOJ2589 보물섬 20210319 pypy3으로 통과함
import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,m,li,pos):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    visited = [[False for _ in range(m)] for __ in range(n)]
    r,c = pos
    q = deque([(r,c,0)])
    visited[r][c] = True
    mx = 0
    while q:
        r,c,cnt = q.popleft()
        mx = max(mx,cnt)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and li[nr][nc] == "L":
                    visited[nr][nc] = True
                    q.append((nr,nc,cnt+1))
    return mx

def main():
    n,m = map(int,input().rstrip().split())
    li = [list(input().rstrip()) for _ in range(n)]
    mx = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] == "L":
                mx = max(bfs(n, m, li, (i,j)), mx)
    
    print(mx)
if __name__ == '__main__':
    main()