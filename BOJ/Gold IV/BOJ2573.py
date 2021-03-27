#BOJ2573 빙산 20210327
import sys
from collections import deque
input = sys.stdin.readline

li = []
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def melt(r,c):
    ice = li[r][c]
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if li[nr][nc] == 0: cnt += 1
    ice -= cnt
    return 0 if ice < 0 else ice    

def bfs(r,c):
    cnt = 0
    q = deque()
    visited = set()
    visited.add((r,c))
    q.append((r,c))
    while q:
        cnt += 1
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if li[nr][nc] != 0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc))
    return cnt
def main():
    global li
    n,m = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    ice = []
    for i in range(n):
        for j in range(m):
            if li[i][j] != 0:
                ice.append((i,j))
    year = 0
    cnt = len(ice)
    while True:
        if cnt == 0: return print(0)
        r,c= ice[0]
        if cnt != bfs(r,c) : return print(year)
        nextIce = []
        for r,c in ice:
            leftIce = melt(r,c)
            nextIce.append((r,c,leftIce))
        ice = []
        for r,c,i in nextIce:
            li[r][c] = i
            if li[r][c] != 0: ice.append((r,c))
        cnt = len(ice)
        year += 1

if __name__ == '__main__':
    main()