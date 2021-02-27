#BOJ7562 나이트의 이동 20210227
import sys
from collections import deque
input = sys.stdin.readline

def main():
    for __ in range(int(input())):
        n = int(input())
        s = tuple(map(int, input().rstrip().split()))
        e = tuple(map(int, input().rstrip().split()))
        q = deque()
        q.append(s)
        dx = [1,2,2,1,-1,-2,-2,-1]
        dy = [2,1,-1,-2,-2,-1,1,2]
        visited = {tuple(s):0}
        while q:
            tmp = q.popleft()
            for i in range(8):
                x = tmp[0] + dx[i]
                y = tmp[1] + dy[i]
                if 0 <= x < n and 0 <= y < n:
                    if (x,y) not in visited:
                        q.append((x,y))
                        visited[(x,y)] = visited[tmp] + 1
            if e in visited:
                break
        print(visited[e])
if __name__ == '__main__':
    main()