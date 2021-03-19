#BOJ5014 스타트링크 20210317
import sys
from collections import deque
input = sys.stdin.readline

def main():
    f,s,g,u,d = map(int, input().rstrip().split())
    visited = [False] * (f+1)
    q = deque()
    q.append((s,0))
    while q:
        floor, cnt = q.popleft()
        if floor == g:
            return print(cnt) 
        for v in [u,-d]:
            nfloor = floor + v
            if 0 < nfloor <= f:
                if not visited[nfloor]:
                    visited[nfloor] = True
                    q.append((nfloor, cnt+1))
    print("use the stairs")
if __name__ == '__main__':
    main()