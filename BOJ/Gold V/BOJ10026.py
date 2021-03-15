#BOJ10026 적록색약 20210315
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]
def bfs(p,li,visited,n,weak):
    q = deque()
    q.append(p)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if weak:
                    if ((li[y][x] in ['R','G'] and li[ny][nx] in ['R','G']) or li[y][x] == li[ny][nx]) and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx,ny))
                else:
                    if li[y][x] == li[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx,ny))
def solve(n,li,weak):
    visited = [[False for _ in range(n)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs((j,i), li, visited, n, weak)
                cnt += 1
    return cnt

def main():
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    print(solve(n,li,False), solve(n,li,True))
if __name__ == '__main__':
    main()