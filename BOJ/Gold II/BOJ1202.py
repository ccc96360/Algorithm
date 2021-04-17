#BOJ1202 보석 도둑 20210417
import sys
import heapq as hq
input = sys.stdin.readline

WEIGHT = 0
COST = 1
def main():
    n,k = map(int,input().rstrip().split())
    gem = [list(map(int,input().rstrip().split())) for _ in range(n)]
    gem.sort(key=lambda x:x[WEIGHT])
    bag = [int(input()) for _ in range(k)]
    bag.sort()
    ans = idx = 0
    q = []
    for v in bag:
        while idx < n and v >= gem[idx][WEIGHT]:
            hq.heappush(q,(-gem[idx][COST]))
            idx += 1
        if q:
            ans += -hq.heappop(q)
    print(ans)

if __name__ == '__main__':
    main()