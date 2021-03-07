#BOJ2583 영역 구하기 20210307
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

FILL = True
EMPTY = False

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(p, n, m, li, visited, res):
    global dx,dy
    res[0] += 1
    x = p[0]
    y = p[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < m and 0 <= nx < n:
            np = (nx, ny)
            if np not in visited and li[ny][nx] == EMPTY:
                visited.add(np)
                dfs(np, n, m, li, visited, res)


def main():
    m,n,k = map(int,input().rstrip().split())
    li = [[EMPTY for _ in range(n)] for __ in range(m)]
    for _ in range(k):
        points = list(map(int,input().rstrip().split()))
        for i in range(points[1],points[3]):
            for j in range(points[0],points[2]):
                li[i][j] = FILL
    visited = set()
    ans = []; cnt = 0
    for i in range(m):
        for j in range(n):
            p = (j, i)
            res = [0]
            if p not in visited and li[i][j] == EMPTY:
                cnt += 1
                visited.add(p)
                dfs(p, n, m, li, visited, res)
                ans.append(res[0])
    ans.sort()
    print(cnt)
    print(*ans)
if __name__ == '__main__':
    main()