#BOJ1938 통나무 옮기기 20210423
import sys
from collections import deque
input = sys.stdin.readline

li = []
U,D,L,R,T = [0,1,2,3,4]

def canMove(pos,n,dir):
    if dir != T:
        for r,c in pos:
            if 0 <= r < n and 0 <= c < n:
                if li[r][c] == "1":
                    return False
            else:
                return False
    else:
        dr = [-1,-1,-1,0,0,0,1,1,1]
        dc = [-1,0,1,-1,0,1,-1,0,1]
        r,c = pos[1]
        for i in range(9):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if li[nr][nc] == "1":
                    return False
            else: return False
    return True

def move(pos,dir):
    return {U: moveUp,
        D: moveDown,
        L: moveLeft,
        R: moveRight,
        T: moveTurn,        
    }[dir](pos)
    
def moveUp(pos):
    nextPos = list(map(lambda x: (x[0]-1,x[1]), pos))
    return nextPos

def moveDown(pos):
    nextPos = list(map(lambda x: (x[0]+1,x[1]), pos))
    return nextPos

def moveLeft(pos):
    nextPos = list(map(lambda x: (x[0],x[1]-1), pos))
    return nextPos

def moveRight(pos):
    nextPos = list(map(lambda x: (x[0],x[1]+1), pos))
    return nextPos

def moveTurn(pos):
    nextPos = [0,pos[1],0]
    if pos[0][0] == pos[2][0]:
        nextPos[0] = (pos[1][0]-1, pos[1][1])
        nextPos[2] = (pos[1][0]+1, pos[1][1])
    elif pos[0][1] == pos[2][1]:
        nextPos[0] = (pos[1][0], pos[1][1]-1)
        nextPos[2] = (pos[1][0], pos[1][1]+1)
    return nextPos
def main():
    global li
    n = int(input())
    li = [list(input().rstrip()) for _ in range(n)]
    s,e = [],[]
    for i in range(n):
        for j in range(n):
            if li[i][j] == "E":
                e.append((i,j))
            elif li[i][j] == "B":
                s.append((i,j))
    q = deque()
    q.append((s,0))
    visited = set()
    visited.add(tuple(s))
    while q:
        v,cnt = q.popleft()
        if v == e:
            return print(cnt)
        for dir in [U,D,L,R,T]:
            nv = move(v,dir)
            if canMove(nv,n,dir) and tuple(nv) not in visited:
                visited.add(tuple(nv))
                q.append((nv,cnt+1))
    print(0)
if __name__ == '__main__':
    main()