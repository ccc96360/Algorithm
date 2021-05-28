#BOJ11967 블켜기 20210528
import sys
from collections import deque
input = sys.stdin.readline

def inScope(x,y,n):
    return 1 <= x <= n and 1 <= y <= n

def main():
    n, m = map(int, input().rstrip().split())
    info = {}
    for _ in range(m):
        x,y,a,b = map(int, input().rstrip().split())
        if (x,y) not in info:
            info[(x,y)] = [(a,b)]
        else:
            info[(x,y)].append((a,b))
    visited = set([(1,1)])
    lightedRoom = set([(1,1)])
    q = deque([(1,1)])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        x,y = q.popleft()
        if (x,y) in info:
            for a,b in info[(x,y)]:
                lightedRoom.add((a,b))
                if (a,b) not in visited:
                    for i in range(4):
                        pa = a + dx[i]
                        pb = b + dy[i]
                        if inScope(pa,pb,n) and (pa,pb) in visited:
                            visited.add((a,b))
                            q.append((a,b))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if inScope(nx,ny,n) and (nx,ny) not in visited:
                if (nx,ny) in lightedRoom:
                    visited.add((nx,ny))
                    q.append((nx,ny))
    print(len(lightedRoom))

if __name__ == '__main__':
    main()