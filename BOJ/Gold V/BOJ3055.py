#BOJ3055 탈출 20210317
import sys
from collections import deque
input = sys.stdin.readline

def main():
    r,c = map(int, input().rstrip().split())
    li = [list(input().rstrip()) for _ in range(r)]
    water = []
    gosum = ""
    d = ""
    for i in range(r):
        for j in range(c):
            if li[i][j] == "S":
                gosum = [(i,j)]
                li[i][j] = "S0"
            if li[i][j] == "*":
                water.append((i,j))
                li[i][j] = "*0"
            if li[i][j] == "D":
                d = (i,j)
    waterQ = deque(water)
    q = deque(gosum)
    time = 0
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    flag = False
    while q or waterQ:
        if flag: break
        while waterQ:
            wr,wc = waterQ[0]
            if li[wr][wc] != "*"+str(time): break
            waterQ.popleft()
            for i in range(4):
                nwr = wr + dr[i]
                nwc = wc + dc[i]
                if 0 <= nwr < r and 0 <= nwc < c:
                    if li[nwr][nwc] == ".":
                        li[nwr][nwc] = "*"+str(time+1)
                        waterQ.append((nwr,nwc))
        while q:
            sr,sc = q[0]
            if li[sr][sc] != "S"+str(time): break
            q.popleft()
            for i in range(4):
                nsr = sr + dr[i]
                nsc = sc + dc[i]
                if 0 <= nsr < r and 0 <= nsc < c:
                    if li[nsr][nsc] == "D":
                        li[nsr][nsc] = time+1
                        flag = True
                    if li[nsr][nsc] == ".":
                        li[nsr][nsc] = "S"+str(time+1)
                        q.append((nsr,nsc))
        time += 1    
    '''
    for v in li:
        print(v)'''
    print("KAKTUS" if li[d[0]][d[1]] == "D" else li[d[0]][d[1]])
if __name__ == '__main__':
    main()