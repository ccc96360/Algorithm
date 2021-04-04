#BOJ2146 다리만들기 20210404 
import sys
from collections import deque
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(r,c,li,visited,n):
    q = deque()
    q.append((r,c))
    res = set()
    while q:
        r,c = q.popleft()
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if li[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    cnt += 1
                elif li[nr][nc] == 0:
                    res.add((r,c))
    return list(res)
def main():
    n = int(input())
    li = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for __ in range(n)]
    island = []
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and li[r][c] == 1:
                visited[r][c] = True
                island.append(bfs(r,c,li,visited,n))
    n = len(island)
    res = sys.maxsize
    for i in range(n):
        for j in range(i+1,n):
            for r1,c1 in island[i]:
                for r2,c2 in island[j]:
                    res = min(res,abs(r1-r2)+abs(c1-c2)-1)
    print(res)
if __name__ == '__main__':
    main()