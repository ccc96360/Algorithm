#BOJ14442 벽 부수고 이동하기 2 20210412 PyPy3로 제출함
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,m,k = map(int,input().rstrip().split())
    li = [list(map(int,list(input().rstrip()))) for _ in range(n)]
    dp = [[[0 for ___ in range(k+1)] for __ in range(m)] for _ in range(n)]
    dp[0][0][0] = 1
    q = deque()
    breakedWall = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    q.append((0,0,breakedWall))
    while q:
        cr, cc, breakedWall = q.popleft()
        if cr == n-1 and cc == m-1:
            return print(dp[cr][cc][breakedWall])
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if dp[nr][nc][breakedWall] == 0:
                    if li[nr][nc] == 0:
                        dp[nr][nc][breakedWall] = dp[cr][cc][breakedWall] + 1
                        q.append((nr,nc,breakedWall))
                    elif breakedWall < k and dp[nr][nc][breakedWall+1] == 0:
                        dp[nr][nc][breakedWall+1] = dp[cr][cc][breakedWall] + 1
                        q.append((nr,nc,breakedWall + 1))
    print(-1)
if __name__ == '__main__':
    main()