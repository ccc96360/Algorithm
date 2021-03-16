#BOJ14499 주사위 굴리기 20210316
import sys
from collections import deque
input = sys.stdin.readline

class Dice:
    def __init__(self,x,y):
        self.garo = deque([0,0,0,0])#b,l,t,r
        self.sero = deque([0,0,0,0])#u,t,d,b   
        self.x = x
        self.y = y
    def moveRight(self):
        t = self.garo.pop()
        self.garo.appendleft(t)
        self.synchronize(1)
        self.x += 1

    def moveLeft(self):
        t = self.garo.popleft()
        self.garo.append(t)
        self.synchronize(1)
        self.x -= 1

    def moveDown(self):
        t = self.sero.pop()
        self.sero.appendleft(t)
        self.synchronize(2)
        self.y += 1

    def moveUp(self):
        t =self.sero.popleft()
        self.sero.append(t)
        self.synchronize(2)
        self.y -= 1

    def move(self, dir):
        {1 : self.moveRight, 2 : self.moveLeft, 3 : self.moveUp, 4 : self.moveDown}[dir]()
    def rollback(self, dir):
        {2 : self.moveRight, 1 : self.moveLeft, 4 : self.moveUp, 3 : self.moveDown}[dir]()

    def synchronize(self,t):
        if t == 1:
            self.sero[1] = self.garo[2]
            self.sero[3] = self.garo[0]
        elif t == 2:
            self.garo[2] = self.sero[1]
            self.garo[0] = self.sero[3]

    def setBottom(self, n):
        self.garo[0] = n
        self.sero[3] = n

    def getTop(self):
        return self.garo[2]

    def getBottom(self):
        return self.garo[0]

    def getPos(self):
        return (self.x, self.y)
def main():
    n, m, x, y, k = map(int, input().rstrip().split())
    dice = Dice(y,x)
    li = []
    for _ in range(n):
        li.append(list(map(int, input().rstrip().split())))
    cmd = list(map(int, input().rstrip().split()))
    for c in cmd:
        dice.move(c)
        x,y = dice.getPos()
        if 0 <= y < n and 0 <= x < m:
            if li[y][x] == 0:
                li[y][x] = dice.getBottom()
            else:
                dice.setBottom(li[y][x])
                li[y][x] = 0
            print(dice.getTop())
        else:
            dice.rollback(c)
if __name__ == '__main__':
    main()