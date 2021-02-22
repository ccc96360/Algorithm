#BOJ11053 가장 긴 증가하는 부분 수열 20210222
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        max_ = 0
        for j in range(i):
            if li[i] > li[j] and dp[j] > max_:
                max_ = dp[j]
        dp[i] = max_ + 1
    print(max(dp))
if __name__ == '__main__':
    main()