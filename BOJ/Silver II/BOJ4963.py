#BOJ4963 섬의 개수 20210225
import sys
from collections import deque
input = sys.stdin.readline

def main():
    while True:
        w,h = map(int, input().rstrip().split())
        if w == 0 and h == 0: break
        li = [list(map(int, input().rstrip().split())) for _ in range(h)]
        visited = [[False for _ in range(w)] for __ in range(h)]
        cnt = 0
        for i in range(h):
            for j in range(w):
                if li[i][j] == 0 or visited[i][j]: continue
                cnt += 1
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                dx = [1,-1, 0, 0, 1, 1, -1, -1]
                dy = [0, 0, 1, -1, 1, -1, 1, -1]
                while q:
                    tmp = q.popleft()
                    for k in range(8):
                        x = tmp[1] + dx[k]
                        y = tmp[0] + dy[k]
                        if 0 <= x < w and 0 <= y <h:
                            if li[y][x] == 1 and not visited[y][x]:
                                visited[y][x] = True
                                q.append([y,x])
        print(cnt)
if __name__ == '__main__':
    main()