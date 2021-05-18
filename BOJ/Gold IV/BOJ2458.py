#BOJ2458 키 순서 20210518 PyPy3으로 제출함
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().rstrip().split())
    floyd = [[0 for _ in range(n)] for __ in range(n)]
    for _ in range(m):
        a,b = map(lambda x : int(x) - 1, input().rstrip().split())
        floyd[a][b] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if floyd[i][k] == 1 and floyd[k][j] == 1:
                    floyd[i][j] = 1

    ret = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if floyd[j][i] == 1 or floyd[i][j] == 1:
                cnt += 1
        if cnt == n-1:
            ret += 1
    print(ret)
if __name__ == '__main__':
    main()