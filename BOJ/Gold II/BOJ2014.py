#BOJ2014 소수의 곱 20210423
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    n,k = map(int,input().rstrip().split())
    li = list(map(int,input().rstrip().split()))
    q = []
    qSize = 0
    exist = set()
    for v in li:
        hq.heappush(q, v)
        exist.add(v)
        qSize += 1
    mx = li[-1]
    for _ in range(k-1):
        v = hq.heappop(q)
        qSize -= 1
        for x in li:
            if qSize > k and v*x > mx:
                continue
            if v*x not in exist:
                mx = max(mx, v*x)
                exist.add(v*x)
                hq.heappush(q, v*x)
                
                qSize += 1
    print(hq.heappop(q))

if __name__ == '__main__':
    main()