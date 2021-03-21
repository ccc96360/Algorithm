#BOJ9019 DSLR 20210321
import sys
from collections import deque
input = sys.stdin.readline

class DSLR:
    def __init__(self,n):
        self.num = n
    def cmd(self,c):
        {"D": self.d,
         "S": self.s,
         "L": self.l,
         "R": self.r
        }[c]()

    def d(self):
        self.num = (self.num * 2) % 10000
         

    def s(self):
        a = self.num
        self.num = 9999 if a == 0 else a-1
    
    def l(self):
        a = self.num
        self.num = (a % 1000) * 10 + (a // 1000)
    
    def r(self):
        a = self.num
        self.num = (a%10) * 1000 + (a//10)

    def getNum(self):
        return self.num

def main():
    a,b = map(int,input().rstrip().split())
    q = deque()
    q.append((a,""))
    commands = ["D","S","L","R"]
    visited = [False] * 10001
    visited[a] = True
    while q:
        num, cmd = q.popleft()
        for c in commands:
            tmp = DSLR(num)
            tmp.cmd(c)
            ni = tmp.getNum()
            if ni == b:
                return print(cmd + c)
            if not visited[ni]:
                visited[ni] = True
                q.append((ni, cmd+c))

if __name__ == '__main__':
    for tc in range(int(input())):
        main()