#BOJ11726 2xn 타일링 20210211
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    dp = [1,2]
    if n >= 3:
        for i in range(2,n):
            dp.append((dp[i-1] + dp[i-2])%10007)
    print(dp[n-1])
if __name__ == '__main__':
    main()