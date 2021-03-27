#BOJ15685 드래곤 커브 20210327
import sys
input = sys.stdin.readline

class DragonCurve:
    def __init__(self, x, y, d):
        self.startPoint = (y,x) # r,c
        self.endPoint = (y+[0,-1,0,1][d], x+[1,0,-1,0][d])
        self.dir = d
        self.points = [self.startPoint, self.endPoint]
        self.gen = 0
    def nextGen(self):
        self.gen += 1
        n = len(self.points)
        for i in range(n-2,-1,-1):
            r,c = self.points[i]
            self.points.append(self.rotate90(r,c))
        self.endPoint = self.points[-1]

    def getGen(self):
        return self.gen
    def rotate90(self,r,c):
        er,ec = self.endPoint
        tr = r - er
        tc = c - ec

        tmp = tc
        tc = -tr
        tr = tmp
        
        tr += er
        tc += ec
        return (tr,tc)
def main():
    curves = []
    gen = []
    n = int(input())
    for _ in range(n):
        x,y,d,g = map(int,input().rstrip().split())
        curves.append(DragonCurve(x,y,d))
        gen.append(g)

    points = set()
    for i in range(n):
        while curves[i].getGen() != gen[i]:
            curves[i].nextGen()
        points.update(curves[i].points)
    
    res = 0
    for v in points:
        r,c = v
        if (r+1,c+1) in points and (r,c+1) in points and (r+1,c) in points:
            res += 1
    print(res)
if __name__ == '__main__':
    main()
