#BOJ1753 최단경로 20210312
import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 2**30

def dijkstra(adj, start, weights):
    heap = []
    heapq.heappush(heap, [weights[start], start])
    while heap:
        weight, v = heapq.heappop(heap)
        print(weight,v)
        if weights[v] < weight: continue
        for nv, w in adj[v]:
            if weights[nv] > weight + w:
                weights[nv] = weight + w
                heapq.heappush(heap, [weights[nv], nv])

def main():
    n,m = map(int, input().rstrip().split())
    start = int(input())
    adj = [ [] for _ in range(n+1)]
    weights = [INF for _ in range(n+1)]
    weights[start] = 0
    for _ in range(m):
        u,v,w = map(int, input().rstrip().split())
        adj[u].append((v,w))
    dijkstra(adj, start, weights)
    for i in range(1,n+1):
        v = weights[i]
        print(v if v != INF else "INF")
if __name__ == '__main__':
    main()