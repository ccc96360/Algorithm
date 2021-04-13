#BOJ2252 줄 세우기 20210413
from collections import deque
import sys
input = sys.stdin.readline

def topologySort(n, inDegree, adj):
    q = deque()
    ret = []
    for v in range(n):
        if inDegree[v] == 0:
            q.append(v)
    while q:
        v = q.popleft()
        ret.append(v)
        for nv in adj[v]:
            inDegree[nv] -= 1
            if inDegree[nv] == 0:
                q.append(nv)
    return ret

def main():
    n,m = map(int,input().rstrip().split())
    inDegree = [0] * n
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(lambda x : int(x)-1, input().rstrip().split())
        adj[a].append(b)
        inDegree[b] += 1
    topology = topologySort(n, inDegree, adj)
    ans = list(map(lambda x: x+1, topology))
    print(*ans)    

if __name__ == '__main__':
    main()