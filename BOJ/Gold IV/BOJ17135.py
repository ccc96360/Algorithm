#BOJ17135 캐슬 디펜스 20210515
import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

CANT_ATTACK = (-1,-1)
def attack(archer, enemies, d):
    dist = sys.maxsize
    ret = CANT_ATTACK
    for e in enemies:
        tmp = distance(archer, e)
        if tmp <= d and tmp <= dist:
            if tmp == dist:
                if ret[1] > e[1]:
                    ret = e
            else:
                ret = e
            dist = tmp
    return ret

def main():
    n,m,d = map(int,input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    enemiesOrigin = set()
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                enemiesOrigin.add((i,j))

    ans = 0
    for archers in combinations([(n,i) for i in range(m)],3):
        enemies = deepcopy(enemiesOrigin)
        numOfDeadEnemy = 0
        while enemies:
            deleteEnemy = set()
            for archer in archers:
                tmp = attack(archer, enemies, d)
                if tmp != CANT_ATTACK: deleteEnemy.add(tmp)
            for v in deleteEnemy:
                enemies.remove(v)
                numOfDeadEnemy += 1

            tmp = set()
            for r,c in enemies:
                if r+1 < n: tmp.add((r+1,c))
            enemies = tmp
        ans = max(ans, numOfDeadEnemy)
    print(ans)
if __name__ == '__main__':
    main()