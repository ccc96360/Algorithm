#BOJ1766 문제집 20210415
import sys
import heapq as hq
input = sys.stdin.readline

def topologySort(n,adj,indegree):
    q = []
    res = []
    for v in range(n):
        if indegree[v] == 0:
            hq.heappush(q,v)
    while q:
        v = hq.heappop(q)
        res.append(v)
        for nv in adj[v]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                hq.heappush(q,nv)
    return res

def main():
    n,m = map(int,input().rstrip().split())
    adj = [[] for _ in range(n)]
    indegree = [0] * (n)
    for _ in range(m):
        a,b = map(lambda x: int(x)-1,input().rstrip().split())
        adj[a].append(b)
        indegree[b] += 1
    topology = list(map(lambda x: x+1, topologySort(n, adj, indegree)))
    print(*topology)

if __name__ == '__main__':
    main()