#BOJ11051 이항 계수 2 20210308
import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    li = [[1 for _ in range(i+1)] for i in range(n+1)]
    for i in range(2,n+1):
        for j in range(i):
            if j == 0: continue
            li[i][j] = (li[i-1][j] + li[i-1][j-1]) % 10007
    print(li[n][k])


if __name__ == '__main__':
    main()