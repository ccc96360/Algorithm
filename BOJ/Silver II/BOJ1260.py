#BOJ1260 DFS와 BFS 20210222
import sys
from collections import deque
input = sys.stdin.readline

def dfs(adj, visited, v):
    visited[v] = True
    print(v, end = " ")
    for i in adj[v]:
        if not visited[i]:
            dfs(adj, visited, i)
def bfs(adj, visited, q):
    while q:
        tmp = q.popleft()
        if visited[tmp]: continue
        visited[tmp] = True
        print(tmp, end =" ")
        for i in adj[tmp]:
            if not visited[i]:
                q.append(i)

def main():
    n,m,v = map(int, input().rstrip().split())
    adj = [[] for i in range(n+1)]
    visited = [False for _ in range(n+1)]
    q = deque([v])
    for _ in range(m):
        a,b = map(int, input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    for i in range(n):
        adj[i+1].sort()
    dfs(adj,visited,v)
    visited = [False for _ in range(n+1)]
    print()
    bfs(adj, visited, q)
if __name__ == '__main__':
    main()