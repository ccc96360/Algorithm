#BOJ16235 나무 재테크 20210330 PyPy3 으로 제출함, 너무 빡빡한 문제
import sys
from collections import deque
input = sys.stdin.readline

ALIVE = 0
DEAD = 1

dr = [0,0,-1,1,1,1,-1,-1]
dc = [-1,1,0,0,-1,1,-1,1]

class Land:
    def __init__(self):
        self.aliveTrees = deque()
        self.nutrient = 5
        self.refillNutrient = 0
        self.aliveTreeNum = 0

    def setAliveTrees(self, trees, num):
        self.aliveTrees = deque(trees)
        self.aliveTreeNum = num

    def addAliveTree(self,age):
        self.aliveTreeNum += 1
        self.aliveTrees.append(age)
    
    def addBabyTree(self):
        self.aliveTreeNum += 1
        self.aliveTrees.appendleft(1)

    def getAliveTree(self):
        self.aliveTreeNum -= 1
        return self.aliveTrees.popleft()

    def setRefillNutrient(self,v):
        self.refillNutrient = v

    def refill(self):
        self.nutrient += self.refillNutrient

def main():
    n,m,k = map(int,input().rstrip().split())
    a = [list(map(int,input().rstrip().split())) for _ in range(n)]
    li = [[Land() for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            li[i+1][j+1].refillNutrient = a[i][j]

    for _ in range(m):
        r,c,age = map(int, input().rstrip().split())
        li[r][c].addAliveTree(age)

    for _ in range(k):
        #SPRING & SUMMER
        for r in range(1,n+1):
            for c in range(1,n+1):
                if li[r][c].aliveTrees:
                    land = li[r][c]
                    nextNutrient = 0
                    tmpAliveTrees = []
                    cnt = 0
                    aliveNum = land.aliveTreeNum
                    for __ in range(aliveNum):
                        age = land.getAliveTree()
                        if land.nutrient >= age:
                            land.nutrient -= age
                            tmpAliveTrees.append(age+1)
                            cnt += 1
                        else:
                            nextNutrient += age // 2
                    land.setAliveTrees(tmpAliveTrees,cnt)
                    land.nutrient += nextNutrient
                    li[r][c] = land

        #FALL & WINTER
        for r in range(1,n+1):
            for c in range(1,n+1):
                li[r][c].refill()
                for age in li[r][c].aliveTrees:
                    if age % 5 == 0:
                        for i in range(8):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if 1 <= nr <= n and 1 <= nc <= n:
                                li[nr][nc].addBabyTree()
    ans = 0
    for r in range(1,n+1):
        for c in range(1,n+1):
            ans += li[r][c].aliveTreeNum
    print(ans)
if __name__ == '__main__':
    main()