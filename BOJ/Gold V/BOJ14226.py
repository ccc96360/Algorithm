#BOJ14226 이모티콘 20210513
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())

    visited = set()
    q = deque([(1,0,0)])
    visited.add((1,0))
    while q:
        window, clip, time = q.popleft()
        if window == n:
            print(time)
            break

        if clip != 0 and ((window+clip, clip)) not in visited:
            q.append((window + clip, clip, time + 1))
            visited.add((window+clip, clip))

        if ((window, window)) not in visited:
            q.append((window, window, time + 1))
            visited.add((window, window))

        if window >= 1 and ((window-1, clip)) not in visited:
            q.append((window-1, clip, time + 1))
            visited.add((window-1, clip))
    
if __name__ == '__main__':
    main()