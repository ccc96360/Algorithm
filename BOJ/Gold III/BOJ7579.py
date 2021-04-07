#BOJ7579 앱 20210407
import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split())
    used = [0] + list(map(int,input().rstrip().split()))
    cost = [0] + list(map(int,input().rstrip().split()))
    maxCost = sum(cost)
    dp = [[0 for _ in range(maxCost+1)] for __ in range(n+1)]
    ans = maxCost + 1
    for i in range(1,n+1):
        for j in range(maxCost+1):
            if cost[i] <= j:
                dp[i][j] = max(used[i] + dp[i-1][j-cost[i]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][j] >= m:
                ans = min(ans,j)
    print(ans)
                
if __name__ == '__main__':
    main()