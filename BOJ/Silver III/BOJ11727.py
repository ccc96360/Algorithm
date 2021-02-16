#BOJ11727 2xn 타일링 2 20210216
import sys
input = sys.stdin.readline

def main():
    dp = [1,3]
    for i in range(2,1001):
        dp.append((dp[i-1]+dp[i-2]*2)%10007)
    print(dp[int(input())-1])
if __name__ == '__main__':
    main()