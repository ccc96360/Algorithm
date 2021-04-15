#BOJ1655 가운데를 말해요 20210415
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    n = int(input())
    a = []
    b = []
    hq.heappush(b,int(input()))
    print(b[0])
    maxA = 0
    maxB = 1
    cntA = 0
    cnt = cntB = 1
    for _ in range(n-1):
        k = int(input())
        cnt += 1
        if cnt % 2 == 0: maxB += 1
        else: maxA += 1

        if a and -a[0] > k:
            hq.heappush(a,-k)
            cntA += 1
        else:
            hq.heappush(b,k)
            cntB += 1

        if cntA > maxA:
            tmp = hq.heappop(a)
            cntA -= 1
            hq.heappush(b,-tmp)
            cntB += 1
        elif cntB > maxB: 
            tmp = hq.heappop(b)
            cntB -= 1
            hq.heappush(a,-tmp)
            cntA += 1
        print(b[0])
if __name__ == '__main__':
    main()