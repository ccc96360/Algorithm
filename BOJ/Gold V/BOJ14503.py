#BOJ14503 로봇 청소기 20210313
import sys
input = sys.stdin.readline

class Robot:
    def __init__(self,x,y,dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.cnt = 0
        self.activate = True
    def clean(self):
        self.cnt += 1
        return self.cnt
    def moveForward(self):
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        self.x += dx[self.dir]
        self.y += dy[self.dir]
    def moveBack(self):
        dx = [0,-1,0,1]
        dy = [1,0,-1,0]
        self.x += dx[self.dir]
        self.y += dy[self.dir]
    def turnLeft(self):
        self.dir = {0:3, 1:0, 2:1, 3:2}[self.dir]
    def getLeft(self):
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        return (self.x+dx[self.dir], self.y + dy[self.dir])
    def getBack(self):
        dx = [0,-1,0,1]
        dy = [1,0,-1,0]
        return (self.x + dx[self.dir], self.y + dy[self.dir])
    def getPos(self):
        return (self.x, self.y)
    def isActivate(self):
        return self.activate
    def stop(self):
        self.activate = False
def main():
    n,m = map(int, input().rstrip().split())
    y,x,dir = map(int,input().rstrip().split())
    r = Robot(x,y,dir)
    map_ = [list(map(int,input().rstrip().split())) for _ in range(n)]
    res = 0
    while True:
        if not r.isActivate() : break
        x,y = r.getPos()
        if map_[y][x] == 0: #step 1
            res = r.clean()
            map_[y][x] = 2
        canNotClean = 0
        while True: #step2
            lx,ly = r.getLeft()
            if 0 <= lx < m and 0 <= ly < n:
                if map_[ly][lx] == 0:
                    r.turnLeft()
                    r.moveForward()
                    break
            canNotClean += 1
            r.turnLeft()
            if canNotClean == 4:
                bx,by = r.getBack()
                if map_[by][bx] == 1:
                    r.stop()
                    break
                r.moveBack()
                canNotClean = 0
    print(res)
if __name__ == '__main__':
    main()