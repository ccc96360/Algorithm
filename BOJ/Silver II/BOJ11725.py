#BOJ11725 트리의 부모 찾기 20210228
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n, adj, visited, parent):
    visited[n] = True
    for v in adj[n]:
        if not visited[v]:
            parent[v] = n
            dfs(v, adj, visited, parent)
    visited[n] = False

def main():
    n = int(input())
    adj = [ [] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int, input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (n+1)
    parent = [0] * (n+1)
    dfs(1, adj, visited, parent)
    for i in range(2,n+1): print(parent[i])
if __name__ == '__main__':
    main()