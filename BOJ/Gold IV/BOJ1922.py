#BOJ1922 네트워크 연결 20210325
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    n, m =[int(input()) for _ in range(2)] 
    visited = [False] * (n+1)
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w = map(int, input().rstrip().split())
        adj[a].append((b,w))
        adj[b].append((a,w))
    q = []
    for v,w in adj[1]:
        hq.heappush(q, (w,v))
    visited[1] = True
    res = []
    while q:
        w,v = hq.heappop(q)
        if visited[v]: continue
        visited[v] = True
        res.append(w)
        for nv,nw in adj[v]:
            if not visited[nv]:
                hq.heappush(q, (nw,nv))
    print(sum(res))
if __name__ == '__main__':
    main()