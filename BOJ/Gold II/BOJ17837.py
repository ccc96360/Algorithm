#BOJ17837 새로운 게임 2 20210422
import sys
input = sys.stdin.readline

WHITE, RED, BLUE = 0, 1, 2
RIGHT, LEFT, UP, DOWN = 1,2,3,4
class Piece:
    def __init__(self,r,c,dir,num,h):
        self.r = r
        self.c = c
        self.dir = dir    
        self.num = num
        self.h = h
    def nextPos(self):
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        nr = self.r + dr[self.dir-1]
        nc = self.c + dc[self.dir-1]
        return nr,nc
    def changePos(self,r,c,h):
        self.r = r
        self.c = c
        self.h = h
    def changeDir(self):
        self.dir = {RIGHT:LEFT, LEFT:RIGHT, UP:DOWN, DOWN:UP}[self.dir]

def canMove(r,c,n):
    return 0 <= r < n and 0 <= c < n

def main():
    n,k = map(int,input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    mapInfo = [[[] for _ in range(n)] for __ in range(n)]
    pieces = []
    for _ in range(k):
        r,c,dir = map(int,input().rstrip().split())
        num = len(pieces)
        pieces.append(Piece(r-1,c-1,dir,num,0))
        mapInfo[r-1][c-1].append(num)
    cnt = 0
    while cnt < 1000:
        cnt += 1
        for v in pieces:
            r,c,h,num = v.r, v.c, v.h, v.num
            tmp = mapInfo[r][c][h:]

            nr,nc = v.nextPos()
            flag = 0
            if not canMove(nr,nc,n):
                v.changeDir()
                nr,nc = v.nextPos()
                flag += 1
            if li[nr][nc] == BLUE and flag == 0:
                v.changeDir()
                nr,nc = v.nextPos()
            if canMove(nr,nc,n): 
                if li[nr][nc] in [WHITE,RED]:
                    if li[nr][nc] == RED: tmp.reverse()
                    for t in tmp:
                        mapInfo[r][c].pop()
                        mapInfo[nr][nc].append(t)
                        height = len(mapInfo[nr][nc]) - 1
                        pieces[t].changePos(nr,nc,height)
                if len(mapInfo[nr][nc]) >= 4:
                    return print(cnt)
        
    print(-1)
if __name__ == '__main__':
    main()