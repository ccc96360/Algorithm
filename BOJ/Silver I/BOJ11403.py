#BOJ11403 경로 찾기 20210306
import sys
input = sys.stdin.readline

def dfs(n, adj, res, visited,s):
    for v in adj[n]:
        if not visited[v]:
            res[s][v] = 1
            visited[v] = True
            dfs(v, adj, res, visited, s)


def main():
    n = int(input())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    res = [[0 for __ in range(n)] for _ in range(n)]
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                adj[i].append(j)
    for i in range(n):
        visited = [False] * n
        dfs(i, adj, res, visited,i)
    for i in range(n):
        print(*res[i])
if __name__ == '__main__':
    main()