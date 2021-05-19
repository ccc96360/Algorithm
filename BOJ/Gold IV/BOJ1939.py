#BOJ1939 중량제한 20210519
import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(s, e, adj, res):
    q = []
    for v,w in adj[s]:
        hq.heappush(q, (-w,v))
        res[v] = w
    
    while q:
        w,v = hq.heappop(q)
        w *= -1
        if res[v] > w : continue
        for nv,nw in adj[v]:
            nw = min(w,nw)
            if res[nv] < nw:
                res[nv] = nw
                hq.heappush(q, (-nw,nv))
def main():
    n,m = map(int, input().rstrip().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w = map(int,input().rstrip().split())
        adj[a].append((b,w))
        adj[b].append((a,w))
    s,e = map(int,input().rstrip().split())
    res = [-1] * (n+1)
    res[s] = sys.maxsize
    dijkstra(s,e,adj,res)
    print(res[e])
if __name__ == '__main__':
    main()