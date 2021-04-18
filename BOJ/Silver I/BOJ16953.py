#BOJ16953 A->B 20210418
import sys
from collections import deque
input = sys.stdin.readline

MAX = 10**9
def main():
    a,b = map(int,input().rstrip().split())
    q = deque()
    q.append((a,1))
    action = [lambda x: x*2, lambda x:x*10 + 1]
    visited = set()
    visited.add(a)
    while q:
        v, cnt = q.popleft()
        if v == b:
            return print(cnt)
        for func in action:
            nv = func(v)
            if nv not in visited and nv <= MAX:
                visited.add(nv)
                q.append((nv, cnt+1))
    print(-1)
if __name__ == '__main__':
    main()