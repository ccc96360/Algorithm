#BOJ2714 문자를받은 승환이 20210111
class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
    DIR_LIST = [RIGHT, DOWN, LEFT, UP]
    def __init__(self, dir):
        self.dir = dir
        self.idx = dir
    def changeDir(self):
        self.idx = (self.idx + 1) % 4
        self.dir = Direction.DIR_LIST[self.idx]
    
class Position:
    def __init__(self, x, y,dir):
        self.dir = dir
        self.x = x
        self.y = y
    def nextPos(self):
        if self.dir.dir == Direction.RIGHT:
            self.y += 1
        elif self.dir.dir == Direction.LEFT:
            self.y -= 1
        elif self.dir.dir == Direction.UP:
            self.x -= 1
        elif self.dir.dir == Direction.DOWN:
            self.x += 1

def binTodec(a):
    n = len(a) - 1
    ret = 0
    for i in a:
        if i == "1":
            ret += 2 ** n
        n -= 1
    return ret

def main():
    alphabat = {0 : " "}
    alphabat.update({i+1 : chr(65+i) for i in range(0,26)})
    tc = int(input())
    for __ in range(tc):
        r,c,n = input().split(" ")
        r = int(r); c = int(c)
        li = []
        t = 0
        for i in range(0, len(n)//c):
            li.append(list(n[t:t+c]))
            t += c
        visited =[[False]*c for _ in range(r)]
        cnt = 0
        curPos = Position(0, 0, Direction(Direction.RIGHT))
        res = []
        tmp = ""
        while cnt < r*c:
            cnt += 1
            visited[curPos.x][curPos.y] = True
            tmp += li[curPos.x][curPos.y]
            if len(tmp) == 5:
                res.append(tmp)
                tmp = ""
            if cnt == r*c: break
            prevPos = Position(curPos.x, curPos.y, curPos.dir)
            curPos.nextPos()
            if curPos.x >= r or curPos.y >= c:
                curPos = Position(prevPos.x, prevPos.y, prevPos.dir)
                curPos.dir.changeDir()
                curPos.nextPos()
            if visited[curPos.x][curPos.y] and cnt < r*c:
                curPos = Position(prevPos.x, prevPos.y, prevPos.dir)
                curPos.dir.changeDir()
                curPos.nextPos()
        resStr = ""
        for i in res:
            resStr += alphabat[binTodec(i)]
        print(resStr.rstrip())

if __name__ == '__main__':
    main()