#BOJ2206 벽 부수고 이동하기 20210323
import sys
from collections import deque
input = sys.stdin.readline

NBW = 0 # Not Break Wall 
BW = 1 # Break Wall 

def main():
    r,c = map(int, input().rstrip().split())
    li = [list(map(int, input().rstrip())) for _ in range(r)]
    visited = [[[0,0] for _ in range(c)] for __ in range(r)]
    q = deque()
    q.append((0, 0, False))
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    visited[0][0][NBW] = 1
    while q:
        cr, cc, wallBreaked = q.popleft()
        t = BW if wallBreaked else NBW
        if cr == r-1 and cc == c-1:
            return print(visited[cr][cc][t])
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                if visited[nr][nc][t] == 0:
                    if li[nr][nc] == 0:
                        visited[nr][nc][t] = visited[cr][cc][t] + 1
                        q.append((nr,nc,wallBreaked))
                    elif not wallBreaked and visited[nr][nc][BW] == 0:
                        visited[nr][nc][BW] = visited[cr][cc][t] + 1
                        q.append((nr,nc,True))
    print(-1)
if __name__ == '__main__':
    main()