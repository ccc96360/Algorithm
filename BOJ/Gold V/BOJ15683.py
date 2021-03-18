#BOJ15683 감시 20210318
import sys
input = sys.stdin.readline

mark = 0

class CCTV:
    def __init__(self,pos,type):
        self.pos = pos
        self.type = type
        self.dir = {1:[[1],[2],[3],[4]],
                    2:[[1,3], [2,4]], 
                    3:[[1,2],[3,4],[2,3],[1,4]], 
                    4:[[1,2,3],[1,2,4],[2,3,4],[1,3,4]], 
                    5:[[1,2,3,4]]}[type]
def watch(li,dir,pos,n,m, mark):
    r,c = pos
    cnt = 0
    canNotSee = [mark, 1, 2, 3, 4, 5, 6]
    if dir == 1:#UP
        for i in range(r-1, -1, -1):
            if li[i][c] not in canNotSee:
                li[i][c] = mark
                cnt += 1
            elif li[i][c] == 6:
                break
    elif dir == 2:#right
        for i in range(c+1, m):
            if li[r][i] not in canNotSee:
                li[r][i] = mark
                cnt += 1
            elif li[r][i] == 6:
                break
    elif dir == 3:#down
        for i in range(r+1,n):
            if li[i][c] not in canNotSee:
                li[i][c] = mark
                cnt += 1
            elif li[i][c] == 6:
                break
    elif dir == 4:#left
        for i in range(c-1,-1,-1):
            if li[r][i] not in canNotSee:
                li[r][i] = mark
                cnt += 1
            elif li[r][i] == 6:
                break
    return cnt

def solve(cctv, li, n, m, allcctv):
    global mark
    if not allcctv:
        mark -= 1
        cnt = 0
        for v in cctv:
            for d in v[1]:
                cnt += watch(li, d, v[0], n, m, mark)
        return cnt
    else:
        cnt = 0
        for v in allcctv[0].dir:
            res = solve(cctv + [[allcctv[0].pos, v]], li, n, m, allcctv[1:])
            cnt = max(cnt, res)
        return cnt

def main():
    n, m = map(int, input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    cctv = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] not in [0,6]:
                cctv.append(CCTV((i,j),li[i][j]))
            if li[i][j] == 0:
                cnt += 1
    res = solve([], li, n, m, cctv)
    print(cnt - res)          
if __name__ == '__main__':
    main()