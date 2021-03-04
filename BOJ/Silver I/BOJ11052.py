#BOJ11052 카드 구매하기 20210304
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    p = [0] + list(map(int, input().rstrip().split()))
    dp = [0] + [0] * n
    dp[1] = p[1]
    for i in range(2, n+1):
        max_ = 0
        for j in range(i):
            max_ = max(p[i-j] + dp[j], max_)
        dp[i] = max_
    print(dp[n])
if __name__ == '__main__':
    main()