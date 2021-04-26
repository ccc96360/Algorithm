#BOJ2098 외판원 순회 20210426
import sys
input = sys.stdin.readline

dp = []
INF = sys.maxsize
# v로 시작해 0으로 돌아오는 최소 비용
def dfs(v, visited, n, li):
    global dp
    if visited == (1 << n) - 1:
        if li[v][0] == 0:
            return INF
        else:
            dp[v][1<<0] = li[v][0]
            return li[v][0]
    if dp[v][visited] != INF:
        return dp[v][visited]
    for nv in range(1,n):
        if li[v][nv] != 0 and visited&(1<<nv) == 0:
            dp[v][visited] = min(dp[v][visited], dfs(nv, visited|(1<<nv), n, li) + li[v][nv])
    return dp[v][visited]

def main():
    global dp
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp = [[INF for _ in range(2**n)] for _ in range(n)]
    res = dfs(0, 1 << 0, n, li)
    print(res)
if __name__ == '__main__':
    main()