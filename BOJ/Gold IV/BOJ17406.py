#BOJ17406 배열 돌리기 4 20210519
import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

def rotate(li,r,c,s):
    sr,sc = r-s, c-s
    er,ec = r+s, c+s
    while (sr,sc) != (er,ec):
        tmp = li[sr][ec]
        for tc in range(ec,sc,-1):
            li[sr][tc] = li[sr][tc-1]

        tmp2 = li[er][ec]
        for tr in range(er,sr+1,-1):
            li[tr][ec] = li[tr-1][ec]
        li[sr+1][ec] = tmp
        
        tmp = li[er][sc]
        for tc in range(sc,ec-1):
            li[er][tc] = li[er][tc+1]
        li[er][ec-1] = tmp2

        for tr in range(sr,er-1):
            li[tr][sc] = li[tr+1][sc]
        li[er-1][sc] = tmp
        sr += 1
        sc += 1
        er -= 1
        ec -= 1

def main():
    n,m,k = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    op = [list(map(lambda x: int(x)-1, input().rstrip().split())) for _ in range(k)]

    res = sys.maxsize
    for ops in permutations(op,k):
        tmp = deepcopy(li)
        for r,c,s in ops:
            rotate(tmp, r, c, s + 1)
        for v in tmp:
            res = min(sum(v), res)
    print(res)
if __name__ == '__main__':
    main()