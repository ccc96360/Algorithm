#BOJ2178 미로 탐색 20210301
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    li = [input().rstrip() for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited = {}
    visited[(0,0)] = 1
    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if (nx,ny) not in visited and li[ny][nx] == '1':
                    visited[(nx,ny)] = visited[p] + 1
                    q.append((nx,ny))
    print(visited[(m-1, n-1)])
if __name__ == '__main__':
    main()