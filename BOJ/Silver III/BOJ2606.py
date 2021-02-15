#BOJ2606 바이러스 20210215
import sys
input = sys.stdin.readline

def dfs(n,adj,visited):
    visited[n] = True
    for v in adj[n]:
        if not visited[v]:
            dfs(v,adj,visited)

def main():
    n = int(input().rstrip())
    adj = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for _ in range(int(input())):
        a,b = map(int, input().rstrip().split(" "))
        adj[a].append(b)
        adj[b].append(a)
    dfs(1,adj,visited)
    res = -1
    for v in visited:
        if v == True: res += 1
    print(res)
if __name__ == '__main__':
    main()