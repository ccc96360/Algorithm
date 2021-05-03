#BOJ2169 로봇 조종하기 20210503
import sys
input = sys.stdin.readline

MIN = -sys.maxsize

def main():
    global dp
    n,m = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]

    dp = [[]] + [[MIN for _ in range(m)] for _ in range(n-1)]
    sum_ = 0
    for v in li[0]:
        sum_ += v
        dp[0].append(sum_)

    for i in range(1,n):
        sum_ = 0
        left = [dp[i-1][0] + li[i][0]] + [MIN] * (m-1)
        right = [MIN] * (m-1) + [dp[i-1][-1] + li[i][-1]]
        for j in range(1,m):
            k = m-1-j
            left[j] = max(left[j-1], dp[i-1][j]) + li[i][j]
            right[k] = max(right[k+1], dp[i-1][k]) + li[i][k]
        for j in range(m):
            dp[i][j] = max(left[j], right[j])
    print(dp[-1][-1])
if __name__ == '__main__':
    main()