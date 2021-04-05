#BOJ1167 트리의 지름 20210405
import sys
input = sys.stdin.readline

def dfs(v,adj,visited,ret):
    visited[v] = True
    tmp = ret
    retV = v
    for nv,nw in adj[v]:
        if not visited[nv]:
            t,rv = dfs(nv,adj,visited,tmp+nw)
            if t > ret:
                ret = t
                retV = rv
    visited[v] = False
    return ret,retV

def main():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    for _ in range(n):
        tmp = list(map(int,input().rstrip().split()))
        v,w = 0,0
        for i in range(1,len(tmp)-1):
            if i % 2 == 1:
                v = tmp[i]
            else:
                w = tmp[i]
                adj[tmp[0]].append((v,w))
    visited = [False for _ in range(n+1)]
    nv = dfs(1,adj,visited,0)[1]
    visited = [False for _ in range(n+1)]
    ans = dfs(nv,adj,visited,0)[0]
    print(ans)
        
if __name__ == '__main__':
    main()