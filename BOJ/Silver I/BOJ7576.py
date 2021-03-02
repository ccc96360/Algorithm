#BOJ7576 토마토 20210302
import sys
from collections import deque
input = sys.stdin.readline

def main():
    m,n = map(int, input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    startTomato = []
    zCnt = 0
    for i in range(n):
        for j in range(m):
            v = li[i][j]
            if v == 1: startTomato.append((j,i))
            elif v == 0: zCnt += 1
    q = deque(startTomato)
    visited = { v : 0 for v in startTomato}
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    day = cnt = 0
    while q:
        p = q.popleft()
        day = visited[p]
        for i in range(4):
            x = p[0] + dx[i]
            y = p[1] + dy[i]
            if 0 <= x < m and 0 <= y < n:
                if (x,y) not in visited and li[y][x] == 0:
                    cnt += 1
                    li[y][x] = 1
                    visited[(x,y)] = day + 1
                    q.append((x,y))
    print(-1 if zCnt != cnt else day)
if __name__ == '__main__':
    main()