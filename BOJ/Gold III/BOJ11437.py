#BOJ11437 LCA 20210407
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(v,adj,visited,lev,parent):
    visited[v] = True
    for nv in adj[v]:
        if not visited[nv]:
            lev[nv] = lev[v] + 1
            parent[nv].append(v)
            dfs(nv,adj,visited,lev,parent)

def maxLev(n):
    ret = 1
    while 2 ** ret < n:
        ret += 1
    return ret

def lca(a,b,lev,parent,mxLev):
    if lev[a] > lev[b]:
        a,b = b,a 
    for i in range(mxLev, -1, -1):
        if lev[b] - lev[a] >= 2**i:
            b = parent[b][i]
    if a == b: return a
    for i in range(mxLev, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]
    
def main():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    lev = [0 for _ in range(n+1)]
    parent = [[] for _ in range(n+1)]
    parent[0] = parent[1] = [0]
    for _ in range(n-1):
        a,b = map(int,input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False for _ in range(n+1)]
    dfs(1,adj,visited,lev,parent)
    mxLev= maxLev(n)
    for j in range(1,mxLev+1):
        for i in range(1,n+1):
            parent[i].append(parent[parent[i][j-1]][j-1])

    for i in range(int(input())):
        a,b = map(int,input().rstrip().split())
        print(lca(a,b,lev,parent,mxLev))
if __name__ == '__main__':
    main()