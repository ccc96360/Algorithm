#BOJ14502 연구소 20210312
import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(virus, li, safe, n, m):
    q = deque(virus)
    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if li[ny][nx] == 0:
                    li[ny][nx] = 2
                    q.append((nx,ny))
                    safe -= 1
    return safe
def setWall(li, points):
    for p in points:
        li[p[1]][p[0]] = 1
def removeWall(li, points):
    for p in points:
        li[p[1]][p[0]] = 0

def main():
    n,m = map(int,input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    virus = []
    safeArea = [] 
    safe = n*m - 3
    for i in range(n):
        for j in range(m):
            if li[i][j] == 2: virus.append((j,i))
            elif li[i][j] == 0: safeArea.append((j,i))
            if li[i][j] != 0: safe -= 1
    max_ = 0
    for v in combinations(safeArea,3):
        setWall(li,v)
        max_ = max(max_, bfs(virus, copy.deepcopy(li), safe, n, m)) 
        removeWall(li,v)
    print(max_)
if __name__ == '__main__':
    main()