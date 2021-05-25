#BOJ2662 기업투자 20210525
import sys
from copy import deepcopy
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    benefits = [[0] * m]
    for _ in range(n):
        tmp = list(map(int, input().rstrip().split()))
        benefits.append(tmp[1:])
    dp = [[0 for _ in range(n+1)] for _ in range(m)]
    res = [[[0] * m for _ in range(n+1)] for _ in range(m)]

    for i in range(n+1):
        dp[0][i] = benefits[i][0]
        res[0][i][0] = i
    for i in range(1,m):
        for j in range(n+1):
            mx = dp[i-1][j]
            for cost in range(j):
                if dp[i-1][cost] + benefits[j-cost][i] > mx:
                    mx = dp[i-1][cost] + benefits[j-cost][i]
                    res[i][j] = deepcopy(res[i-1][cost])
                    res[i][j][i] = j-cost
            if mx == dp[i-1][j]:
                res[i][j] = deepcopy(res[i-1][j])
            dp[i][j] = mx
    print(dp[-1][-1])
    print(*res[-1][-1])
    
if __name__ == '__main__':
    main()