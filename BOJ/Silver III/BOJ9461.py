#BOJ9431 파도반 수열 20210216
import sys
input = sys.stdin.readline

def main():
    dp = [1,1,1,2,2]
    for i in range(5,101):
        dp.append(dp[i-1]+dp[i-5])
    for __ in range(int(input())):
        print(dp[int(input())-1])
if __name__ == '__main__':
    main()