#BOJ1261 알고스팟 20210327
import sys
from collections import deque
input = sys.stdin.readline

def main():
    m,n = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip())) for _ in range(n)]
    memo = [[10001 for _ in range(m)] for __ in range(n)]
    q = deque()
    q.append((0,0,0))
    memo[0][0] = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    while q:
        r,c,wall = q.popleft()
        if wall != memo[r][c]: continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                nw = wall
                if li[nr][nc] == 1: nw += 1
                if memo[nr][nc] > nw:
                    memo[nr][nc] = nw
                    q.append((nr,nc,nw))
    print(memo[-1][-1])

if __name__ == '__main__':
    main()