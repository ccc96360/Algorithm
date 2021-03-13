#BOJ9251 LCS 20210313
import sys
input = sys.stdin.readline

def main():
    s1,s2 = map(str, [input().rstrip() for _ in range(2)])
    n,m = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[m][n])
if __name__ == '__main__':
    main()