#BOJ1976 여행 가자 20210517
import sys
input = sys.stdin.readline

def main():
    n,m = [int(input()) for _ in range(2)]
    adj = [list(map(int,input().rstrip().split())) for _ in range(n)]
    li = list(map(lambda x: int(x)-1, input().rstrip().split()))

    floyd = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: floyd[i][j] = 1
            else: floyd[i][j] = adj[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if floyd[i][k] == 1 and floyd[k][j] == 1:
                    floyd[i][j] = 1
    
    flag = False
    for i in range(m-1):
        if floyd[li[i]][li[i+1]] != 1:
            flag = True
            break
    print("NO" if flag else "YES")
if __name__ == '__main__':
    main()