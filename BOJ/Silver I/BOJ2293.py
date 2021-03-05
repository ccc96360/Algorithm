#BOJ2293 동전1 20210305
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().rstrip().split())
    li = [int(input().rstrip()) for _ in range(n)]
    li.sort()
    dp = [1] + [0]*10000
    for coin in li:
        for j in range(1,k+1):
            if j >= coin:
                dp[j] += dp[j-coin]
    print(dp[k])

if __name__ == '__main__':
    main()