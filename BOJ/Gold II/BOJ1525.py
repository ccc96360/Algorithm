#BOJ1525 퍼즐 20210417
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def checkAns(li):
    return li == [1,2,3,4,5,6,7,8,0]

def main():
    li =[]
    for _ in range(3):
        li.extend(list(map(int,input().rstrip().split())))
    idx = 0
    for i in range(9):
        if li[i] == 0: idx = i
    q = deque()
    q.append((idx,li,0))
    visited = set()
    visited.add(tuple(li))
    d = [-1,1,3,-3] # l,r,d,u
    while q:
        idx,li,cnt = q.popleft()
        if checkAns(li):
            return print(cnt)
        for i in range(4):
            if idx % 3 == 0 and i == 0: continue
            if idx % 3 == 2 and i == 1: continue
            nIdx = idx + d[i]
            if 0 <= nIdx < 9:
                tmp = deepcopy(li)
                tmp[idx], tmp[nIdx] = tmp[nIdx], tmp[idx]
                if tuple(tmp) not in visited:
                    visited.add(tuple(tmp))
                    q.append((nIdx, tmp, cnt+1))
    print(-1)
if __name__ == '__main__':
    main()