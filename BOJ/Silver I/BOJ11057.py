#BOJ11057 오르막 수 20210305
import sys
input = sys.stdin.readline

def main():
    dp = [1] * 10
    for i in range(1,int(input())):
        sum_ = 0
        for j in range(10):
            sum_ += dp[j]
            dp[j] = sum_
    print(sum(dp) % 10007)

if __name__ == '__main__':
    main()