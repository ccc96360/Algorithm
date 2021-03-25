#BOJ16236 아기 상어 20210325
import sys
from collections import deque
input = sys.stdin.readline

class Shark:
    def __init__(self,r,c):
        self.r = r
        self.c = c
        self.size = 2
        self.exp = 0
    
    def eat(self):
        self.exp += 1
        if self.exp == self.size:
            self.size += 1
            self.exp = 0
    def move(self,r,c):
        self.r = r
        self.c = c
    def canEat(self, fishSize):
        if fishSize >= self.size or fishSize == 0:
            return False
        return True

    def canMove(self, fishSize):
        if fishSize > self.size:
            return False
        return True

    def getPos(self):
        return (self.r, self.c)

def main():
    n = int(input())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    fishes = [0] * 7
    sr = sc = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] == 9:
                sr,sc = (i,j)
            elif li[i][j] != 0:
                fishes[li[i][j]] += 1
    shark = Shark(sr,sc)
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    time = 0
    while sum(fishes[:shark.size]) != 0:
        q = deque()
        visited = {}
        sr,sc = shark.getPos()
        q.append((sr,sc))
        visited[(sr,sc)] = 0
        candidate = []
        candidateSize = 0
        mn = sys.maxsize
        while q:
            r,c = q.popleft()
            if visited[(r,c)] == mn: continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if shark.canMove(li[nr][nc]) and (nr,nc) not in visited and visited[(r,c)] < mn:
                        visited[(nr,nc)] = visited[(r,c)] + 1
                        if shark.canEat(li[nr][nc]):
                            mn = visited[(nr,nc)]
                            candidate.append((nr,nc))
                            candidateSize += 1
                        else: q.append((nr,nc))
        if candidateSize == 0: break
        candidate.sort(key = lambda x : (x[0],x[1]))
        nr,nc = candidate[0]
        shark.move(nr,nc)
        shark.eat()
        fishes[li[nr][nc]] -= 1
        li[nr][nc] = 0
        li[sr][sc] = 0
        time += visited[(nr,nc)]
    print(time)
if __name__ == '__main__':
    main()