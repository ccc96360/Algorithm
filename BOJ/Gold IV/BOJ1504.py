#BOJ1504 특정한 최단 경로 20210328
import sys
import heapq as hq
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(k, adj, n):
    d = [INF] * (n+1)
    d[k] = 0
    q = []
    hq.heappush(q, (d[k],k))
    while q:
        w,v = hq.heappop(q)
        if d[v] < w: continue
        for nv,nw in adj[v]:
            if d[v] + nw < d[nv]:
                d[nv] = d[v] + nw
                hq.heappush(q,(d[nv],nv))
    return d

def main():
    n,m = map(int,input().rstrip().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w = map(int,input().rstrip().split())
        adj[a].append((b,w))
        adj[b].append((a,w))
    v1,v2 = map(int,input().rstrip().split())
    li1 = dijkstra(1,adj,n)
    li2 = dijkstra(v1,adj,n)
    li3 = dijkstra(v2,adj,n)
    res = min(li1[v1] + li2[v2] + li3[n], li1[v2] + li3[v1] + li2[n])
    print(res if res < INF else -1)

if __name__ == '__main__':
    main()