#BOJ8252 LCS2 20210322
import sys
input = sys.stdin.readline

def main():
    s1,s2 = [input().rstrip() for _ in range(2)]
    n,m = len(s2),len(s1)
    dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    res = []
    r,c = n,m
    while dp[r][c] != 0:
        if dp[r][c] == dp[r][c-1]:
            c -= 1
        elif dp[r][c] == dp[r-1][c]:
            r -= 1
        elif dp[r][c] == dp[r-1][c-1] + 1:
            res.append(s2[r-1])
            r -= 1
            c -= 1
    res.reverse()
    print(dp[-1][-1])
    print("".join(res))

if __name__ == '__main__':
    main()