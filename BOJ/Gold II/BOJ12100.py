#BOJ12100 2048(Easy) 20210414
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

UP,RIGHT,DOWN,LEFT = [0,1,2,3]
dr = [1,0,-1,0]
dc = [0,-1,0,1]
def move(dir, li, n):
    nr = dr[dir]
    nc = dc[dir]
    r = n-1 if dir == DOWN else 0 
    c = n-1 if dir == RIGHT else 0
    ret = 0
    for _ in range(n):
        if dir in [UP,DOWN]:
            r = n-1 if dir == DOWN else 0 
        if dir in [RIGHT,LEFT]:
            c = n-1 if dir == RIGHT else 0
        q = deque()
        while 0 <= r < n and 0 <= c < n:
            if li[r][c] != 0:
                q.append(li[r][c])
            r += nr
            c += nc
        tmp = []
        tmp2 = deque()
        while q:
            v = q.popleft()
            tmp2.append(v)
            if len(tmp2) == 2:
                if tmp2[0] == tmp2[1]:
                    tmp.append(tmp2[0]*2)
                    tmp2 = deque()
                else:
                    tmp.append(tmp2.popleft())
            if not q and tmp2:
                if len(tmp2) == 2 and tmp2[0] and tmp2[1]:
                    tmp.append(tmp2[0]*2)
                else:
                    tmp.extend(tmp2)
        if not tmp: tmp = [0]
        ret = max(ret,max(tmp))
        {UP:fillUp, DOWN:fillDown, RIGHT: fillRight, LEFT: fillLeft}[dir](n,r,c,li,tmp)
        if dir % 2 == 0: c += 1
        else: r += 1
    return ret
def fillUp(n,_,c,li,tmp):
    r = 0
    m = len(tmp)
    while r < n:
        if r < m:
            li[r][c] = tmp[r]
        else:
            li[r][c] = 0
        r += 1

def fillDown(n,_,c,li,tmp):
    r = -1
    for i in range(len(tmp)):
        li[r][c] =  tmp[i]
        r -= 1
    for i in range(n+r+1):
        li[i][c] = 0

def fillLeft(n,r,_,li,tmp):
    c = 0
    m = len(tmp)
    while c < n:
        if c < m:
            li[r][c] = tmp[c]
        else:
            li[r][c] = 0
        c += 1

def fillRight(n,r,_,li,tmp):
    c = -1
    for i in range(len(tmp)):
        li[r][c] = tmp[i]
        c -= 1
    for i in range(n+c+1):
        li[r][i] = 0
def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    q = deque()
    q.append((deepcopy(li),0))
    ans = 0
    while q:
        map_, cnt = q.popleft()
        if cnt >= 5: break
        for dir in [UP,DOWN,LEFT,RIGHT]:
            tmp = deepcopy(map_)
            ans = max(ans, move(dir,tmp,n))
            q.append((deepcopy(tmp),cnt+1))
    print(ans)
if __name__ == '__main__':
    main()