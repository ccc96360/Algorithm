#BOJ13460 구슬 탈출2 20210413
import sys
from collections import deque
input = sys.stdin.readline
li = []
def canMove(r,b,nextR,nextB,rOut,bOut):
    rr,rc = r
    br,bc = b
    nrr, nrc = nextR if not rOut else [br,bc]
    nbr, nbc = nextB if not bOut else [rr,rc]
    nextRed = li[nrr][nrc] if not rOut else "."
    nextBlue = li[nbr][nbc] if not bOut else "."
    if nextRed == "#" and nextBlue == "#":
        return (False, False)
    elif nextBlue == "#":
        if nrr == br and nrc == bc :
            return (False, False)
        else:
            return (True, False)  
    elif nextRed == "#":
        if nbr == rr and nbc == rc:
            return (False, False)
        else:
            return (False, True)
    elif rOut and bOut:
        return (False,False)
    return (True, True)

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def move(dir,r,b):
    rr,rc = r
    br,bc = b
    nr = dr[dir]
    nc = dc[dir]
    rOut = bOut = False
    canMoveRed, canMoveBlue = canMove(r, b, (rr+nr,rc+nc), (br+nr,bc+nc), rOut, bOut)
    while canMoveRed or canMoveBlue:
        if canMoveRed and not rOut: 
            rr += nr
            rc += nc
        if canMoveBlue and not bOut:
            br += nr
            bc += nc
        if li[rr][rc] == "O": rOut = True
        if li[br][bc] == "O": bOut = True
        canMoveRed, canMoveBlue = canMove((rr,rc), (br,bc), (rr+nr,rc+nc), (br+nr,bc+nc), rOut, bOut)
    return ((rr,rc), (br,bc))

def main():
    global li
    n,m = map(int,input().rstrip().split())
    li = [list(input().rstrip()) for _ in range(n)]
    visited = set()
    red = blue = goal = 0
    for i in range(n):
        for j in range(m):
            t = li[i][j]
            if t == "R":
                red = (i,j)
            elif t == "B":
                blue = (i,j)
            elif t == "O":
                goal == (i,j)
    q = deque()
    q.append((red, blue, 0))
    visited.add((red,blue))
    dirs = [0,1,2,3]
    while q:
        r, b, cnt = q.popleft()
        if cnt >= 10: break
        for i in range(4):
            nr,nb = move(dirs[i],r,b)
            rr, rc = nr
            br, bc = nb
            if li[rr][rc] == "O" or li[br][bc] == "O":
                if li[br][bc] != "O":
                    return print(cnt+1)
            elif (nr,nb) not in visited:
                q.append((nr,nb,cnt+1))
                visited.add((nr,nb))
    print(-1)
if __name__ == '__main__':
    main()