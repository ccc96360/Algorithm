#BOJ5557 1학년 20210512
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    dp = [[0 for _ in range(21)] for _ in range(n-1)]
    dp[0][li[0]] = 1
    for i in range(n-2):
        nextNum = li[i+1]
        for j in range(21):
            if j + nextNum <= 20: dp[i+1][j+nextNum] += dp[i][j]
            if j - nextNum >= 0: dp[i+1][j-nextNum] += dp[i][j]
    print(dp[-1][li[-1]])

if __name__ == '__main__':
    main()
