#BOJ1507 궁금한 민호 20210412
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    mustVisited = [[True for _ in range(n)] for __ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k or j == k or i == j: continue
                if li[i][k] + li[k][j] == li[i][j]:
                    mustVisited[i][j] = False
                elif li[i][j] > li[i][k] + li[k][j]:
                    return print(-1)
    sum_ = 0
    for i in range(n):
        for j in range(i,n):
            if mustVisited[i][j]:
                sum_ += li[i][j]
    print(sum_)
if __name__ == '__main__':
    main()