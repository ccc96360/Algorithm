#BOJ1149 RGB거리 20210301
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dp = [tuple(li[0])]
    for i in range(1,n):
        pr, pg, pb = dp[i-1]
        r = min(pg, pb) + li[i][0]
        g = min(pr, pb) + li[i][1]
        b = min(pr, pg) + li[i][2]
        dp.append((r,g,b))
    print(min(dp[-1]))
if __name__ == '__main__':
    main()