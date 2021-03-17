#BOJ1916 최소비용 구하기 20210317
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(adj, start, weights):
    heap = []
    hq.heappush(heap, [weights[start], start])
    while heap:
        w, v = hq.heappop(heap)
        if weights[v] < w: continue
        for nv, nw in adj[v]:
            if w + nw < weights[nv] :
                weights[nv] = w + nw
                hq.heappush(heap, [weights[nv], nv])

def main():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    weights = [INF for _ in range(n+1)]
    for _ in range(int(input())):
        s, e, w = map(int,input().rstrip().split())
        adj[s].append((e,w))
    s,e = map(int,input().rstrip().split())
    weights[s] = 0
    dijkstra(adj, s, weights)
    print(weights[e])
if __name__ == '__main__':
    main()