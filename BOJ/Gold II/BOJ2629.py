#BOJ2629 양팔저울 20210422
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    dp = [[False for _ in range(40001)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for w in range(40001):
            if dp[i][w]:
                dp[i+1][w] = True
                cw = li[i]
                for t in [w-cw,w+cw,cw-w,cw+w]:
                    if 0 <= t <= 40000:
                        dp[i+1][t] = True
    m = int(input())
    for v in list(map(int,input().rstrip().split())):
        print("Y" if dp[-1][v] else "N", end=" ")
if __name__ == '__main__':
    main()