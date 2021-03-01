#BOJ2667 단지번호붙이기 20210301
import sys
from collections import deque
input = sys.stdin.readline

def bfs(p, li, visited):
    n = len(li)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    q = deque()
    q.append(p)
    visited[(p)] = True
    cnt = 0
    while q:
        tmp = q.popleft()
        cnt += 1
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx,ny) not in visited and li[ny][nx] == "1":
                    visited[(nx,ny)] = True
                    q.append((nx,ny))
    return cnt
def main():
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    visited = {}
    res = []
    for i in range(n):
        for j in range(n):
            if li[i][j] == "1" and (j,i) not in visited:
                res.append(bfs((j,i), li, visited))
    res.sort()
    print(len(res))
    for v in res: print(v)
if __name__ == '__main__':
    main()