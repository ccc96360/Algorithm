#BOJ1005 ACM Craft 20210402
import sys
from collections import deque
input = sys.stdin.readline

def topologicalSort(n,inDegree, adj):
    res = []
    visited = [False] * (n+1)
    q = deque()
    for i in range(1,n+1):
        if inDegree[i] == 0:
            q.append(i)
            visited[i] = True
    while q:
        v = q.popleft()
        res.append(v)
        for i in adj[v]:
            inDegree[i] -= 1
            if inDegree[i] == 0 and not visited[i]:
                q.append(i)
    return res
def main():
    n,k = map(int, input().rstrip().split())
    time = [0] + list(map(int,input().rstrip().split()))
    adj = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    for _ in range(k):
        a,b = map(int, input().rstrip().split())
        adj[a].append(b)
        inDegree[b] += 1
    w = int(input())
    topology = topologicalSort(n, inDegree, adj)
    res = [time[i] for i in range(n+1)]
    for v in topology:
        if v == w: break
        for nv in adj[v]:
            res[nv] = max(res[nv], time[nv] + res[v])
    print(res[w])
if __name__ == '__main__':
    for _ in range(int(input())):
        main()