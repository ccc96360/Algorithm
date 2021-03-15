#BOJ15686 치킨 배달 20210315
import sys
from itertools import combinations
input = sys.stdin.readline

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def main():
    n,m = map(int, input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    chicken = []
    house = []
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                house.append((j,i))
            if li[i][j] == 2:
                chicken.append((j,i))
    hNum = len(house)
    min_ = 1300
    for i in range(1,m+1):
        for v in combinations(chicken, i):
            mins = [100] * hNum
            for j in range(hNum):
                for k in range(i):
                    mins[j] = min(mins[j], distance(house[j], v[k]))
            min_ = min(min_, sum(mins))
    print(min_)
if __name__ == '__main__':
    main()