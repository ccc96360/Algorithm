#BOJ15684 사다리 조작 20210330 PyPy3으로 제출함
import sys
from itertools import combinations
input = sys.stdin.readline

def game(ladder,n,h):
    for i in range(1,n+1):
        cursor = i
        for lev in range(1,h+1):
            if ladder[lev][cursor] != 0:
                cursor = ladder[lev][cursor]
        if i != cursor:
            return False
    return True

def isContinuous(foots):
    dic = {}
    for level, v in foots:
        if level in dic:
            if v in dic[level] or v+1 in dic[level]:
                return True
        else:
            dic[level] = set()
        dic[level].add(v)
        dic[level].add(v+1)
    
    return False

def addFoots(ladder, foots):
    for level, v in foots:
        ladder[level][v] = v+1
        ladder[level][v+1] = v

def removeFoots(ladder, foots):
    for level, v in foots:
        ladder[level][v] = 0
        ladder[level][v+1] = 0

def main():
    n,m,h = map(int,input().rstrip().split())
    ladder = [[0 for __ in range(n+1)] for _ in range(h+1)]
    left = set([(i,j) for i in range(1,h+1) for j in range(1,n)])
    tmp = set()
    for _ in range(m):
        a,b = map(int,input().rstrip().split())
        ladder[a][b] = b+1
        ladder[a][b+1] = b
        if b != 1: tmp.add((a,b-1))
        tmp.add((a,b))
        if b != n-1: tmp.add((a,b+1))
    left = left - tmp
    if game(ladder,n,h):
        return print(0)
    for k in range(1,4):
        for v in combinations(left,k):
            if not isContinuous(v):
                addFoots(ladder, v)
                if game(ladder,n,h):
                    return print(k)
                removeFoots(ladder, v)
    print(-1)
if __name__ == '__main__':
    main()