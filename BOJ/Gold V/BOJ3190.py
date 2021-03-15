#BOJ3190 뱀 20210315
import sys
from collections import deque
input = sys.stdin.readline

class Snake:
    def __init__(self):
        self.dir = 1
        self.body = deque()
        self.body.append((1,1))
    def moveHead(self):
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        head = self.body[-1]
        newHead =(head[0] + dr[self.dir], head[1] + dc[self.dir])
        self.body.append(newHead)
        return newHead
    def moveTail(self):
        self.body.popleft()
    def turnLeft(self):
        self.dir = {0:3,3:2,2:1,1:0}[self.dir]
    def turnRight(self):
        self.dir = {0:1,1:2,2:3,3:0}[self.dir]
    def turn(self, x):
        {'L': self.turnLeft, 'D': self.turnRight}[x]()
    def getBody(self):
        return self.body
def main():
    n = int(input())
    k = int(input())
    apples = {tuple(map(int, input().rstrip().split())) : True for _ in range(k)}
    time = 0
    s = Snake()
    l = int(input())
    info = [input().rstrip().split() for _ in range(l)]
    idx = 0
    while True:
        time += 1
        newHead = s.moveHead()
        if not(1<= newHead[0] <= n and 1 <= newHead[1] <= n) or newHead in list(s.getBody())[:-1]:
            break
        if newHead in apples:
            if not apples[newHead]:
                s.moveTail()
            else:
                apples[newHead] = False
        else:
            s.moveTail()
        for i in range(idx,l):
            if int(info[i][0]) != time:
                idx = i
                break 
            s.turn(info[i][1])

    print(time)
if __name__ == '__main__':
    main()