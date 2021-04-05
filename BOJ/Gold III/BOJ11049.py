#BOJ11049 행렬 곱셈 순서 20210405 PyPy3로 제출함
import sys
input = sys.stdin.readline

INF = sys.maxsize

def operationNum(a,b):
    return a[0] * a[1] * b[1]
    

def newMatrix(a,b):
    return (a[0],b[1])

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    dp = [[[0,(0,0)] for _ in range(n)] for _ in range(n)]
    cnt = i = j = 0
    while cnt < n:
        for _ in range(n-cnt):
            v = li[i]
            mn = INF
            for k in range(i,j):
                tmp = dp[i][k][0] + dp[k+1][j][0] + operationNum(dp[i][k][1], dp[k+1][j][1])
                if tmp < mn:
                    mn = tmp
                    v = newMatrix(dp[i][k][1], dp[k+1][j][1])
            dp[i][j] = [mn,v] if i != j else [0,v]
            i += 1
            j += 1
        cnt += 1
        i = 0
        j = cnt
    print(dp[0][n-1][0])
if __name__ == '__main__':
    main()