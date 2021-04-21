#BOJ17472 다리 만들기 2 20210421
import sys
from collections import deque
import heapq as hq
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def getIsland(li,r,c,visited,n,m):
    ret = []
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q:
        r,c = q.popleft()
        ret.append((r,c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and li[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr,nc))
    return ret

def canMakeBridge(li,v1,v2):
    r1,c1 = v1
    r2,c2 = v2

    if r1 == r2:
        if c1 > c2:
            c1, c2 = c2, c1
        for c in range(c1+1, c2):
            if li[r1][c] == 1:
                return False

    if c1 == c2:
        if r1 > r2:
            r1,r2 = r2,r1
        for r in range(r1+1, r2):
            if li[r][c1] == 1:
                return False

    return True

def getPath(island1, island2,li):
    ret = 11
    for v1 in island1:
        r1,c1 = v1
        for v2 in island2:
            r2,c2 = v2
            if r1 == r2 and canMakeBridge(li,v1,v2) and abs(c1-c2)-1 >= 2:
                ret = min(ret,abs(c1-c2) - 1)
            elif c1 == c2 and canMakeBridge(li,v1,v2) and abs(r1-r2)-1 >= 2:
                ret = min(ret, abs(r1-r2) - 1)
    return ret


def main():
    n,m = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]

    visited = [[False for _ in range(m)] for __ in range(n)]
    islands = []
    numOfIsland = 0
    for r in range(n):
        for c in range(m):
            if li[r][c] == 0 or visited[r][c]: continue
            islands.append(getIsland(li,r,c,visited,n,m))
            numOfIsland += 1
    
    adj = [[] for _ in range(numOfIsland)]
    for i in range(numOfIsland):
        for j in range(i+1,numOfIsland):
            w = getPath(islands[i], islands[j], li)
            if w != 11:
                adj[i].append((j,w))
                adj[j].append((i,w))

    visited = [False] * numOfIsland
    q = []
    for v,w in adj[0]:
        hq.heappush(q,(w,v))
    visited[0] = True
    res = []
    while q:
        w,v = hq.heappop(q)
        if visited[v]: continue
        visited[v] = True
        res.append(w)
        for nv,nw in adj[v]:
            if not visited[nv]:
                hq.heappush(q,(nw,nv))

    flag = False
    for v in visited:
        if not v:
            flag = True
            break
    print(-1 if flag else sum(res))

if __name__ == '__main__':
    main()