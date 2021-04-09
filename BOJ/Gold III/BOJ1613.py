#BOJ1613 역사 20210409
import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().rstrip().split())
    dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
    for i in range(1,n+1): dp[i][i] = 1
    for _ in range(k):
        a,b = map(int,input().rstrip().split())
        dp[a][b] = 1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][k] == 1 and dp[k][j] == 1:
                    dp[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dp[i][j] == 1: dp[j][i] = -1
    for _ in range(int(input())):
        a,b = map(int,input().rstrip().split())
        print(-dp[a][b])


if __name__ == '__main__':
    main()