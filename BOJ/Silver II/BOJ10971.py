#BOJ10971 외판원 순회 2 20210228
import sys
input = sys.stdin.readline

def dfs(parent, n, adj, visited, weights, sum, start, res):
    visited[n] = True   
    sum += weights[parent][n]
    if visited.count(True) == len(visited) and weights[n][start] != 0:
        sum += weights[n][start]
        res.append(sum)
    for v in adj[n]:
        if not visited[v]:
            dfs(n, v, adj, visited, weights, sum, start, res)
    visited[n] = False
def main():
    n = int(input())
    weights = [list(map(int,input().rstrip().split())) for _ in range(n)]
    adj = [[] for _ in range(n)]
    visited=[False] * n
    res = []
    for i in range(n):
        for j in range(n):
            if weights[i][j] != 0 : adj[i].append(j)
    for i in range(n):
        dfs(i, i, adj, visited, weights, 0, i, res)
    print(min(res))
if __name__ == '__main__':
    main()