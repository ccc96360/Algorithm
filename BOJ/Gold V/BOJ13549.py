#BOJ13549 숨바꼭질3 20210511
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, k = map(int,input().rstrip().split())
    q = deque()
    if n > k:
        return print(n-k)
    q.append((n,0))
    visited = {}
    visited[n] = 0
    f = [lambda x: x-1, lambda x: x+1, lambda x:2*x]
    dt = [1,1,0]
    while q:
        location, time = q.popleft()
        if time > visited[location]:
            continue
        if location == k:
            print(time)
            break
        for i in range(3):
            nextLocation = f[i](location)
            nextTime = time + dt[i]
            if 0 <= nextLocation <= 100000 and (nextLocation not in visited or visited[nextLocation] > nextTime):
                visited[nextLocation] = nextTime
                q.append((nextLocation, nextTime))
if __name__ == '__main__':
    main()