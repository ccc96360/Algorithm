#BOJ17143 낚시왕 20210416
import sys
input = sys.stdin.readline

UP, DOWN, RIGHT, LEFT = [1,2,3,4]
def moveSharks(map_,sharks, maxR, maxC):
    tmp = []
    for k,v in sharks.items():
        r,c = k
        map_[r][c] = 0
        s,d,z = v
        nr,nc,nd = nextPos(r,c,s,d,maxR,maxC)
        tmp.append((nr,nc,s,nd,z))
    newSharks = {}
    for r,c,s,d,z in tmp:
        map_[r][c] = 1
        if (r,c) not in newSharks:
            newSharks[(r,c)] = (s,d,z)
        else:
            _,_,cz = newSharks[(r,c)]
            if cz < z:
                newSharks[(r,c)] = (s,d,z)
    return newSharks

def nextPos(r,c,s,d,maxR,maxC):
    nr,nc,nd = r,c,d
    if d == UP:
        amt = r - s
        nr,nc,nd = nextPos(1,c,1-amt,DOWN,maxR,maxC) if amt < 1 else (amt,c,d)
    elif d == DOWN:
        amt = r + s
        nr,nc,nd = nextPos(maxR,c,amt-maxR,UP,maxR,maxC) if amt > maxR else (amt,c,d)
    elif d == RIGHT:
        amt = c + s
        nr,nc,nd = nextPos(r, maxC, amt-maxC, LEFT,maxR,maxC) if amt > maxC else (r,amt,d)
    elif d == LEFT:
        amt = c - s
        nr,nc,nd = nextPos(r, 1, 1-amt, RIGHT,maxR,maxC) if amt < 1 else (r,amt,d)
    return nr,nc,nd

def main():
    maxR,maxC,m = map(int,input().rstrip().split())
    map_ = [[0 for _ in range(maxC+1)] for __ in range(maxR+1)]
    sharks = {}
    for _ in range(m):
        sr,sc,s,d,z = map(int,input().rstrip().split())
        map_[sr][sc] = 1
        sharks[(sr,sc)] = (s,d,z)
    res = 0
    for c in range(1,maxC+1):
        ## step2
        for r in range(1,maxR+1):
            if map_[r][c] != 0:
                s,d,z = sharks[(r,c)]
                res += z
                map_[r][c] = 0
                del sharks[(r,c)]
                break
        ## step3
        sharks = moveSharks(map_, sharks, maxR, maxC)
    print(res)
if __name__ == '__main__':
    main()