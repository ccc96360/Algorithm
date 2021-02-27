#BOJ11279 최대 힙 20210227
import sys
import heapq
input = sys.stdin.readline

def main():
    li = []
    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            if not li:
                print(0)
            else:
                print(heapq.heappop(li) * -1)
        else:
            heapq.heappush(li,n*-1)

if __name__ == '__main__':
    main()