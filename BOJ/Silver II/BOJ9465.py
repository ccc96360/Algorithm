#BOJ9465 스티커 20210224
import sys
input = sys.stdin.readline

UP = 0
DOWN = 1
def main():
    for _ in range(int(input())):
        n = int(input())
        li = [list(map(int, input().rstrip().split()))]
        li.append(list(map(int, input().rstrip().split())))
        dp = [[li[UP][0]],[li[DOWN][0]]]
        if n > 2:
            dp[UP].append(dp[DOWN][0]+li[UP][1])
            dp[DOWN].append(dp[UP][0]+li[DOWN][1])
            for i in range(2,n):
                dp[UP].append(max(max(dp[UP][i-2],dp[DOWN][i-2]),dp[DOWN][i-1])+li[UP][i])
                dp[DOWN].append(max(max(dp[DOWN][i-2],dp[UP][i-2]),dp[UP][i-1])+li[DOWN][i])
        print(max(max(dp[UP][-1],dp[DOWN][-1]),max(dp[UP][-2],dp[DOWN][-2])))
if __name__ == '__main__':
    main()