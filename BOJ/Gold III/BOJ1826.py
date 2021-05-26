#BOJ1826 연료 채우기 20210526
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    n = int(input())
    li = sorted([list(map(int, input().rstrip().split())) for _ in range(n)], key = lambda x : x[0])
    goal, leftOil = map(int, input().rstrip().split())
    curLoc = 0
    q = []
    idx = 0
    res = 0
    while curLoc + leftOil < goal:
        curLoc += leftOil
        leftOil = 0
        while idx < n and li[idx][0] <= curLoc:
            hq.heappush(q, -li[idx][1])
            idx += 1
        if q:
            leftOil = hq.heappop(q) * -1
            res += 1
        elif not q and curLoc + leftOil < goal:
            res = -1
            break
    print(res)
if __name__ == '__main__':
    main()