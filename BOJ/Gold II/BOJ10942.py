#BOJ10942 팰린드롬? 20210414
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[n-1][n-1] = 1
    for i in range(n-1):
        dp[i][i] = 1
        if li[i] == li[i+1]:
            dp[i][i+1] = 1
    for k in range(2,n+1):
        for i in range(n):
            if i+k < n:
                if li[i] == li[i+k]:
                    dp[i][i+k] = dp[i+1][i+k-1]

    for _ in range(int(input())):
        s,e = map(lambda x: int(x)-1,input().rstrip().split())
        print(dp[s][e])
if __name__ == '__main__':
    main()