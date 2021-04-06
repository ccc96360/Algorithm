#BOJ1516 게임 개발 20210406
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def topologicalSort(n, indegree, adj):
    visited = [False] * n
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
            visited[i] = True
    ret = []
    while q:
        v = q.popleft()
        ret.append(v)
        for nv in adj[v]:
            indegree[nv] -= 1
            if not visited[nv] and indegree[nv] == 0:
                q.append(nv)
                visited[nv] = True
    return ret
def main():
    n = int(input())
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    time = [0] * n
    for i in range(n):
        li = list(map(int,input().rstrip().split()))
        time[i] = li[0]
        for v in li[1:]:
            if v != -1:
                adj[v-1].append(i)
                indegree[i] += 1
    topology = topologicalSort(n, indegree, adj)
    res = deepcopy(time)
    for v in topology:
        for nv in adj[v]:
            res[nv] = max(res[v] + time[nv], res[nv])
    for v in res:
        print(v)
if __name__ == '__main__':
    main()