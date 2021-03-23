#BOJ2580 스도쿠 20210323 pypy3로 제출함
import sys
input = sys.stdin.readline

li = []

def isValid(r,c,v):
    for i in range((r//3)*3, (r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            if li[i][j] == v: return False
    for i in range(9):
        if li[r][i] == v: return False
        if li[i][c] == v: return False
    return True

def dfs(blank):
    global li
    if not blank:
        for v in li:
            print(*v)
        exit()
    r,c,can = blank[0]
    for v in can:
        if isValid(r,c,v):
            li[r][c] = v
            dfs(blank[1:])
            li[r][c] = 0


def main():
    global li
    li = [list(map(int, input().rstrip().split())) for _ in range(9)]
    blank = []
    for i in range(9):
        for j in range(9):
            if li[i][j] == 0:
                tmp = set()
                for ii in range((i//3)*3, (i//3)*3+3):
                    for jj in range((j//3)*3, (j//3)*3+3):
                        tmp.add(li[ii][jj])
                for ii in range(9):
                    tmp.add(li[i][ii])
                    tmp.add(li[ii][j])
                can = []
                for v in range(1,10):
                    if v not in tmp:
                        can.append(v)
                blank.append((i,j,can))
    dfs(blank)
if __name__ == '__main__':
    main()