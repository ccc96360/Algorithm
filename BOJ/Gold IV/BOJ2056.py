#BOJ2056 작업 20210402
import sys
from collections import deque
input = sys.stdin.readline

def topologicalSort(n,indegree,adj):
    res = []
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        res.append(v)
        for nv in adj[v]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                q.append(nv)
    return res

def main():
    n = int(input())
    indegree = [0] * n
    time = [0] * n
    adj = [[] for _ in range(n)]
    for i in range(n):
        tmp = list(map(int,input().rstrip().split()))
        time[i] = tmp[0]
        indegree[i] = tmp[1]
        for j in range(indegree[i]):
            adj[tmp[2+j] - 1].append(i)

    topology = topologicalSort(n, indegree, adj)
    res = [time[i] for i in range(n)]
    for v in topology:
        for nv in adj[v]:
            res[nv] = max(res[nv], time[nv] + res[v])
    print(max(res))

if __name__ == '__main__':
    main()