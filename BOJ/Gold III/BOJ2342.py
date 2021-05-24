#BOJ2342 Dance Dance Revlolution 20210524
import sys
input = sys.stdin.readline

def getWeight(prev, next):
    if prev == 0:
        return 2
    elif prev in [2,4] and next in [1,3]:
        return 3
    elif prev in [1,3] and next in [2,4]:
        return 3
    elif next == [3,4,1,2][prev-1]:
        return 4
    elif prev == next:
        return 1
    
INF = sys.maxsize

def main():
    li = list(map(int, input().rstrip().split()))
    dp = [[[INF for _ in range(5)] for _ in range(5)]]
    dp[0][li[0]][0] = 2
    dp[0][0][li[0]] = 2
    for v in li[1:]:
        if v == 0: break
        tmp = [[INF for _ in range(5)] for _ in range(5)]
        for l in range(5):
            for r in range(5):
                if dp[-1][l][r] != INF:
                    if v != r : tmp[v][r] = min(tmp[v][r], dp[-1][l][r] + getWeight(l,v))
                    if v != l : tmp[l][v] = min(tmp[l][v], dp[-1][l][r] + getWeight(r,v))
        dp.append(tmp)
    min_ = INF
    for v in dp[-1]:
        min_ = min(min_, min(v))
    print(min_)

if __name__ == '__main__':
    main()