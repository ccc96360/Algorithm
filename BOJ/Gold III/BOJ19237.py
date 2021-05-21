#BOJ19237 어른 상어 20210521
import sys
input = sys.stdin.readline

UP,DOWN,LEFT,RIGHT = [1,2,3,4]
drc = {
    UP : (-1,0),
    DOWN : (1,0),
    LEFT : (0,-1),
    RIGHT : (0,1)
}
class Shark:
    def __init__(self, loc, num, dir):
        self.loc = loc
        self.num = num
        self.dir = dir
        self.priority = {}
    def setPriority(self, dir,li):
        self.priority[dir] = li
    def move(self, loc, dir):
        self.loc = loc
        self.dir = dir
def main():
    n,m,maxDuration = map(int, input().rstrip().split())
    li = [list(map(int, input().rstrip().split())) for _ in range(n)]
    sharks = {}
    dirs = list(map(int,input().rstrip().split()))
    smells = {}
    for r in range(n):
        for c in range(n):
            if li[r][c] != 0:
                sharks[li[r][c]] = Shark((r,c), li[r][c], dirs[li[r][c]-1])
                smells[(r,c)] = [li[r][c],maxDuration]
    for i in range(1,m+1):
        for dir in [UP,DOWN,LEFT,RIGHT]:
            sharks[i].setPriority(dir, list(map(int, input().rstrip().split())))

    time = 0
    while time < 1001:
        # print("===={0}초====".format(time))
        # print("상어들: {0}======".format([i.num for i in sharks.values()]))
        # print("냄새들: {0}======".format(smells))
        sharkLoc = {}
        if len(sharks) == 1:
            return print(time)
        # Move Shark
        for shark in sharks.values():
            # print("==={0}번 상어 Move".format(shark.num))
            findEmptySmell = False
            # Check Around Smell
            for dir in shark.priority[shark.dir]:
                dr,dc = drc[dir]
                nr = shark.loc[0] + dr
                nc = shark.loc[1] + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr,nc) not in smells:
                        # print("==={0}에 냄새 없음 이동함".format((nr,nc)))
                        shark.move((nr,nc), dir)
                        findEmptySmell = True
                        if (nr,nc) not in sharkLoc:
                            sharkLoc[(nr,nc)] = [shark.num]
                        else:
                            sharkLoc[(nr,nc)].append(shark.num)
                        break
            # Find My Smell
            if not findEmptySmell:
                # print("=== 빈 냄새 없음 내 냄새로 이동함")
                for dir in shark.priority[shark.dir]:
                    dr,dc = drc[dir]
                    nr = shark.loc[0] + dr
                    nc = shark.loc[1] + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if (nr,nc) in smells and smells[(nr,nc)][0] == shark.num:
                            # print("=== {0}에 내냄새 발견 이동함".format((nr,nc)))
                            shark.move((nr,nc), dir)
                            if (nr,nc) not in sharkLoc:
                                sharkLoc[(nr,nc)] = [shark.num]
                            else:
                                sharkLoc[(nr,nc)].append(shark.num)
                            break
        # Delete Smell
        nSmells = {}
        for k,v in smells.items():
            v[1] -= 1
            if v[1] != 0:
                nSmells[k] = v
        smells = nSmells
        # Delete Shark & Add Smell
        for k,v in sharkLoc.items():
            mn = min(v)
            smells[k] = [mn, maxDuration]
            for vv in v:
                if vv > mn:
                    sharks.pop(vv)

        time += 1
    print(-1)
if __name__ == '__main__':
    main()

