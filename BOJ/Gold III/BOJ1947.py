#BOJ1647 선물 전달 20210528
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [0,1]
    for i in range(3,n+1,1):
        dp.append((i-1) * (dp[-1]+dp[-2]) % 1000000000)
    print(dp[n-1])
if __name__ == '__main__':
    main()