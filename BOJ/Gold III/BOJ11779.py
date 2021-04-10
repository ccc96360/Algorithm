#BOJ11779 최소비용 구하기 2 20210410
import sys
import heapq as hq
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(s,adj,n):
    d = [INF] * n
    d[s] = 0
    p = [-1] * n
    q = []
    hq.heappush(q,(d[s],s))
    while q:
        w,v = hq.heappop(q)
        if d[v] < w: continue
        for nv,nw in adj[v]:
            if d[nv] > w + nw:
                d[nv] = w + nw
                p[nv] = v
                hq.heappush(q,(d[nv], nv))
    return d,p
def main():
    n, m = [int(input()) for _ in range(2)]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b,w = map(int,input().rstrip().split())
        adj[a-1].append((b-1,w))
    s,e = map(lambda x: int(x)-1, input().rstrip().split())
    d,p = dijkstra(s,adj,n)
    res = [e]
    idx = p[e]
    while idx != -1:
        res.append(idx)
        idx = p[idx]
    res.reverse()
    res = list(map(lambda x: x+1, res))
    print(d[e])
    print(len(res))
    print(*res)

if __name__ == '__main__':
    main()