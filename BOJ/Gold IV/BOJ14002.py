#BOJ14002 가장 긴 증가하는 부분 수열 4 20210415
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int,input().rstrip().split()))
    tmp = [li[0]]
    tmpSize = 1
    p = []
    for v in li:
        if tmp[-1] < v:
            tmp.append(v)
            p.append(tmpSize)
            tmpSize += 1
        else:
            idx = bisect_left(tmp,v)
            p.append(idx)
            tmp[idx] = v
    print(tmpSize)
    res = []
    for i in range(n-1,-1,-1):
        if p[i] == tmpSize-1:
            res.append(li[i])
            tmpSize -= 1
    res.reverse()
    print(*res)
    
if __name__ == '__main__':
    main()