#BOJ13565 침투 20210608
import sys
from collections import deque
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(r, c, visited, li, n, m):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        if r == n-1:
            return True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <n and 0 <= nc < m:
                if li[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr,nc))
                    visited[nr][nc] = True
    return False
def main():
    n, m = map(int, input().rstrip().split())
    li = [list(map(int, list(input().rstrip()))) for _ in range(n)]

    visited = [[False] * m  for _ in range(n)]
    canGo = False
    for c in range(m):
        if li[0][c] == 0 and not visited[0][c]: 
            canGo = bfs(0, c, visited, li, n, m)
        if canGo: break
    print("YES" if canGo else "NO")
if __name__ == '__main__':
    main()