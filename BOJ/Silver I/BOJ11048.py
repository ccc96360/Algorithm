#BOJ11048 이동하기 20210308
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp[0][0] = li[0][0]
    dx = [-1,0,-1]
    dy = [0,-1,-1]
    for i in range(n):
        for j in range(m):
            max_ = 0
            for k in range(3):
                a = j + dx[k]
                b = i + dy[k]
                if 0 <= a < m and 0 <= b < n:
                    max_ = max(max_, dp[b][a])
            dp[i][j] = max_ + li[i][j]
    print(dp[-1][-1])
if __name__ == '__main__':
    main()