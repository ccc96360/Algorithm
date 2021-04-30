#BOJ1700 멀티탭 스케줄링 20210430
import sys
from collections import deque
input = sys.stdin.readline

def out(multitap, itemLoc):
    mx = [0,0]
    for v in multitap:
        if not itemLoc[v]:
            mx[0] = v
            break            
        else:
            if itemLoc[v][0] > mx[1]:
                mx = [v,itemLoc[v][0]]
    # print("멀티탭에서 {0}빠짐".format(mx[0]))
    multitap.remove(mx[0])
    
def add(multitap, v, itemLoc):
    multitap.add(v)
    itemLoc[v].popleft()
    # print("멀티탭에 {0}꽂음 다음 {0}위치 {1}".format(v,itemLoc[v]))
def main():
    n,m = map(int,input().rstrip().split())
    q = deque(map(int,input().rstrip().split()))
    itemLoc = {}
    for i in range(m):
        v = q[i]
        if v in itemLoc:
            itemLoc[v].append(i)
        else:
            itemLoc[v] = deque([i])

    multitap = set()
    usableCnt = n

    ret = 0
    while q:
        # print(multitap, q, itemLoc)
        v = q.popleft()
        if v not in multitap:
            if usableCnt > 0:
                add(multitap, v, itemLoc)
                usableCnt -= 1
            else:
                out(multitap, itemLoc)
                add(multitap, v, itemLoc)
                ret += 1
        else:
            itemLoc[v].popleft()
    print(ret)
        
if __name__ == '__main__':
    main()
    
