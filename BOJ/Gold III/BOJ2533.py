#BOJ2533 사회망 서비스(SNS) 20210411
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

adj = []
visited = []
dp = []
def setDPTable(v):
    global dp
    for nv in adj[v]:
        if not visited[nv]:
            visited[nv] = True
            setDPTable(nv)
            dp[v][0] += min(dp[nv][0], dp[nv][1])
            dp[v][1] += dp[nv][0]
    dp[v][0] += 1

def main():
    global adj, visited, dp
    n = int(input())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    dp = [[0,0] for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[1] = True
    setDPTable(1)
    print(min(dp[1]))
if __name__ == '__main__':
    main()