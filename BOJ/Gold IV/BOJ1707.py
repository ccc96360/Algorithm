#BOJ1707 이분 그래프 20210326
import sys
from collections import deque
input = sys.stdin.readline

RED = 0
BLACK = 1
EMPTY = 2

def isBipartite(v,adj, visited, n):
    q = deque()
    q.append(v)
    visited[v] = RED
    switch = lambda x : (x - 1) * -1
    while q:
        v = q.popleft()
        color = visited[v]
        for nv in adj[v]:
            if visited[nv] == EMPTY:
                visited[nv] = switch(color)
                q.append(nv)
            elif visited[nv] == color:
                return False
    return True

def main():
    n,m = map(int, input().rstrip().split())
    adj = [[] for _ in range(n+1)]
    visited = [EMPTY] * (n+1)
    for _ in range(m):
        a,b = map(int, input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    for v in range(1,n+1):
        if visited[v] == EMPTY:
            if not isBipartite(v, adj, visited, n):
                return print("NO")
    print("YES")
    
if __name__ == '__main__':
    for _ in range(int(input())):
        main()