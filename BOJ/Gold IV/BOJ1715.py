#BOJ1715 카드 정렬하기 20210504
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    n = int(input())
    q = [int(input()) for _ in range(n)]
    hq.heapify(q)
    ret = 0
    for _ in range(n-1):
        a = hq.heappop(q)
        b = hq.heappop(q)
        ret += a+b
        hq.heappush(q, a+b)
    print(ret)

if __name__ == '__main__':
    main()