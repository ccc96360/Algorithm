#BOJ12865 평범한 배낭 20210316
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().rstrip().split())
    li = [[0,0]] + [list(map(int, input().rstrip().split())) for _ in range(n)]
    li.sort(key= lambda x: x[0])
    dp = [[0 for _ in range(k+1)] for __ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if li[i][0] > j:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), li[i][1]+dp[i-1][j-li[i][0]])
    print(dp[n][k])
if __name__ == '__main__':
    main()