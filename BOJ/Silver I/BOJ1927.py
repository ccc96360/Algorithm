#BOJ1927 최소 힙 20210308
import sys
import heapq as hq
input = sys.stdin.readline

def main():
    q = []
    for _ in range(int(input())):
        cmd = int(input())
        if cmd == 0:
            try:
                print(hq.heappop(q))
            except IndexError:
                print(0)
        else:
            hq.heappush(q,cmd)        


if __name__ == '__main__':
    main()