#BOJ1389 케빈 베이컨의 6단계 법칙 20210311
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    q = deque()
    res = [[0 for __ in range(n+1)] for _ in range(n+1)]
    min_ = 5000
    ans = 1
    for i in range(1,n+1):
        q.append(i)
        visited = [False] * (n+1)
        visited[i] = 0
        while q:
            tmp = q.popleft()
            for v in adj[tmp]:
                if visited[v] == 0 and v != i:
                    visited[v] = visited[tmp] + 1
                    res[i][v] = visited[v]
                    q.append(v)
        s = sum(res[i])
        if s < min_:
            min_ = s
            ans = i
    print(ans)
if __name__ == '__main__':
    main()