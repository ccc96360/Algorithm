#BOJ2623 음악프로그램 20210420
import sys
from collections import deque
input = sys.stdin.readline

def topologySort(n,indegree,adj):
    ret = []
    size = 0
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        ret.append(v)
        size += 1
        for nv in adj[v]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                q.append(nv)
    return ret,size

def main():
    n,m = map(int,input().rstrip().split())
    indegree = [0] * (n)
    adj = [[] for _ in range(n)]
    exist = set()
    for _ in range(m):
        size, *tmp = map(int,input().rstrip().split())
        for i in range(size-1):
            v = tmp[i] - 1
            nv = tmp[i+1] - 1
            if (v,nv) not in exist:
                exist.add((v,nv))
                adj[v].append(nv)
                indegree[nv] += 1
    topology,size = topologySort(n,indegree,adj)
    if size == n:
        for v in topology:
            print(v+1)  
    else:
        print(0)
if __name__ == '__main__':
    main()