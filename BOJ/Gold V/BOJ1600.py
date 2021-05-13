#BOJ1600 말이 되고픈 원숭이 20210513
import sys
from collections import deque
input = sys.stdin.readline

def main():
    k = int(input())
    m,n = map(int,input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]

    
    hdr = [-2,-1,1,2,2,1,-1,-2]
    hdc = [1,2,2,1,-1,-2,-2,-1]
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    visited = [[[(False ,0)  for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

    q = deque([(0, 0, k, 0)])
    visited[0][0][k] = (True, 0)
    while q:
        r, c, k, cnt = q.popleft()
        if k > 0:
            for i in range(8):
                nr = r + hdr[i]
                nc = c + hdc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc][k-1][0] and li[nr][nc] != 1:
                        q.append((nr, nc, k-1, cnt + 1))
                        visited[nr][nc][k-1] = (True, cnt + 1)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc][k][0] and li[nr][nc] != 1:
                    q.append((nr, nc, k, cnt + 1))
                    visited[nr][nc][k] = (True, cnt + 1)

    mn = sys.maxsize                
    for visit, v in visited[n-1][m-1]:
        if visit:
            mn = min(mn, v)
    if mn != sys.maxsize:
        print(mn)
    else:
        print(-1)
if __name__ == '__main__':
    main()