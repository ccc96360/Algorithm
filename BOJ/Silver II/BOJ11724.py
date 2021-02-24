#BOJ11724 연결 요소의 개수 20210224
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    adj = [ [] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    q = deque()
    cnt = 0
    visited = [ False for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i] : continue
        q.append(i)
        visited[i] = True
        cnt += 1
        while q:
            tmp = q.popleft()
            for j in adj[tmp]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True
    print(cnt)
if __name__ == '__main__':
    main()