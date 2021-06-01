import sys
INF = sys.maxsize

def solution(n, s, p1, p2, fares):
    floyd = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for c,d,f in fares:
        floyd[c][d] = f
        floyd[d][c] = f
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j: floyd[i][j] = 0
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
    res = INF
    for i in range(1,n+1):
        a = floyd[i][p1] if i <= p1 else floyd[p1][i]
        b = floyd[i][p2] if i <= p2 else floyd[p2][i]
        res = min(res, (floyd[s][i] if s <= i else floyd[i][s]) + a + b)
    return res

def main():
    n,s,a,b = 6,4,5,6
    fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    print(solution(n,s,a,b,fares))
if __name__ == '__main__':
    main()