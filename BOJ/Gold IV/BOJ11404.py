#BOJ11404 플로이드 20210326
import sys
input = sys.stdin.readline

INF = sys.maxsize

def print_(floyd,n):
    for i in range(1,n+1):
        for j in range(1,n):
            print(floyd[i][j] if floyd[i][j] != INF else 0, end=" ")
        print(floyd[i][n] if floyd[i][n] != INF else 0)


def main():
    n,m = [int(input().rstrip()) for _ in range(2)]
    adj = [[] for _ in range(n+1)]
    floyd = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        a,b,w = map(int,input().rstrip().split())
        adj[a].append(b)
        floyd[a][b] = min(floyd[a][b], w)
    for i in range(1,n+1): floyd[i][i] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    print_(floyd, n)

if __name__ == '__main__':
    main()
