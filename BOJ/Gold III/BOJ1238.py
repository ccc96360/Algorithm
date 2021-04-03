#BOJ1238 파티 20210403
import sys
import heapq as hq
input = sys.stdin.readline

INF = sys.maxsize

adj = []

def dijkstra(s, n):
    d = [INF] * (n+1)
    d[s] = 0
    q = []
    hq.heappush(q, (d[s],s))
    while q:
        w,v = hq.heappop(q)
        if  d[v] < w: continue
        for nv,nw in adj[v]:
            if d[nv] > d[v] + nw:
                d[nv] = d[v] + nw
                hq.heappush(q,(d[nv],nv))
    return d
def main():
    global adj
    n,m,x = map(int,input().rstrip().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w = map(int,input().rstrip().split())
        adj[a].append((b,w))
    xToN = dijkstra(x,n)
    for i in range(1,n+1):
        xToN[i] += dijkstra(i,n)[x]
    print(max(xToN[1:]))
if __name__ == '__main__':
    main()