#BOJ2294 동전 2 20210309
import sys
input = sys.stdin.readline

def main():
    n,k = map(int, input().rstrip().split())
    coin = list(set(int(input().rstrip()) for _ in range(n)))
    coin.sort()
    dp = [[0,0,0]] + [[10001 for _ in range(n)] for __ in range(k)]
    min_ = [0] + [10001 for _ in range(k)]
    for j in range(len(coin)):
        v = coin[j]
        if v > k: break
        for i in range(1,k+1):
            if v > i:
                if j == 0:
                    dp[i][j] = -1
                else:
                    dp[i][j] = min_[i] if min_[i] != 10001 else -1
            else:
                if j == 0 and i % v != 0:
                    dp[i][j] = -1
                else:
                    tmp = min_[i-v]
                    if tmp == 10001: dp[i][j] = -1
                    else: dp[i][j] = 1 + tmp
            if dp[i][j] != -1:
                min_[i] = min(min_[i], dp[i][j])
    print(min_[i] if min_[i] != 10001 else -1)
if __name__ == '__main__':
    main()