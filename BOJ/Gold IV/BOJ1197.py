#BOJ1197 최소 스패닝 트리 20210324 프림알고리즘
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    v,e = map(int,input().rstrip().split())
    adj = [[] for _ in range(v+1)]
    for _ in range(e): 
        a,b,w = map(int,input().rstrip().split())
        adj[a].append((b,w))
        adj[b].append((a,w))
    
    q = []
    res = []
    visited = [False] * (v+1)
    for v,w in adj[1]:
        hq.heappush(q,(w,v))
    visited[1] = True
    while q:
        w,v = hq.heappop(q)
        if visited[v]: continue
        visited[v] = True
        res.append(w)
        for nv,nw in adj[v]:
            if not visited[nv]:
                hq.heappush(q,(nw,nv))
    print(sum(res))
if __name__ == '__main__':
    main()