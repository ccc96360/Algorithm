#BOJ14891 톱니바퀴 20210309
import sys
input = sys.stdin.readline
class Gear:
    CW = 1
    CCW = -1
    def __init__(self, status, n):
        self.status = status
        self.num = n
    def rotate(self, dir):
        if dir == Gear.CW:
            self.status = self.status[7] + self.status[:7]
        elif dir == Gear.CCW:
            self.status = self.status[1:] + self.status[0]
    def getRight(self):
        return self.status[2]
    def getLeft(self):
        return self.status[-2]
    def getScore(self):
        return int(self.status[0]) * (2 ** (self.num-1))
def main():
    gears = [Gear(input().rstrip(), i + 1) for i in range(4)]
    for _ in range(int(input())):
        n,dir = map(int, input().rstrip().split())
        n -= 1
        dirs = [0,0,0,0]
        dirs[n] = dir
        for i in range(n,3):
            if gears[i].getRight() != gears[i+1].getLeft(): dirs[i+1] = -dirs[i]
        for i in range(n,0,-1):
            if gears[i].getLeft() != gears[i-1].getRight(): dirs[i-1] = -dirs[i]
        for i in range(4):
            gears[i].rotate(dirs[i])
    res = [gears[i].getScore() for i in range(4)]
    print(sum(res))
        
if __name__ == '__main__':
    main()