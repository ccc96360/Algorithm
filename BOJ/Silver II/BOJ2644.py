#BOJ2644 촌수계산 20210228
import sys
input = sys.stdin.readline

def dfs(n, end, cnt, adj, visited, res):
    visited[n] = True
    if n == end:
        res.append(cnt)
    for v in adj[n]:
        if not visited[v]:
            dfs(v, end, cnt+1, adj, visited, res)
    visited[n] = False
def main():
    n = int(input())
    s,e = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(int(input())):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (n+1)
    res = []
    dfs(s, e, 0, adj, visited, res)
    print(res[0] if res else -1)
if __name__ == '__main__':
    main()