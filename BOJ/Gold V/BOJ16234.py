#BOJ16234 인구 이동 20210318 pypy3로 통과함
import sys
from collections import deque
input = sys.stdin.readline

def bfs(li, visited, start, n, mn, mx):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    r,c = start
    visited[r][c] = True
    sum = li[r][c]
    union = [(r,c)]

    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and mn <= abs(li[r][c] - li[nr][nc]) <=mx:
                    visited[nr][nc] = True
                    q.append((nr,nc))
                    union.append((nr,nc))
                    sum += li[nr][nc]

    pop = sum // len(union)
    for r,c in union:
        li[r][c] = pop
    if len(union) > 1: return True
    return False
def main():
    n, l, r = map(int, input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    cnt = 0
    while True:
        flag = False
        visited = [[False for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(li, visited, (i,j), n, l, r):
                        flag = True
        if not flag: break
        cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()