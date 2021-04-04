#BOJ11066 파일 합치기 20210404
#PyPy3으로 통과함 Python3 로 통과하려면 크누스 최적화 적용해야함
import sys
input = sys.stdin.readline

INF = sys.maxsize

def main():
    n = int(input())
    li = list(map(int, input().rstrip().split()))
    dp = [[0 for _ in range(n)] for __ in range(n)]
    sums = []
    sum_ = 0
    for v in li:
        sum_ += v
        sums.append(sum_)
    t = 0
    cnt = n - 1
    while t != n-1:
        t += 1
        tmp = cnt
        i = 0
        j = t
        for _ in range(tmp):
            min_ = INF
            for k in range(i,j):
                min_ = min(min_,dp[i][k]+dp[k+1][j])
            dp[i][j] = min_ + sums[j] - sums[i] + li[i]
            i += 1
            j += 1
        cnt -= 1
    print(dp[0][n-1])
if __name__ == '__main__':
    for i in range(int(input())):
        main()