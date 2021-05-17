#BOJ4485 녹색 옷 입은 애가 젤다지? 20210517
import sys
import heapq as hq
input = sys.stdin.readline

INF = sys.maxsize
def main():
    problem = 0
    while True:
        problem += 1
        n = int(input())
        if n == 0: break
        li = [list(map(int, input().rstrip().split())) for _ in range(n)]
        q = []
        hq.heappush(q, (li[0][0], (0,0)))
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        ans = 0
        visited = [[INF for _ in range(n)] for __ in range(n)]
        while q:
            w, p = hq.heappop(q)
            r,c = p
            if visited[r][c] < w: continue
            if (r,c) == (n-1,n-1):
                ans = w
                break
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if visited[nr][nc] > w + li[nr][nc]:
                        visited[nr][nc] = w + li[nr][nc]
                        hq.heappush(q, (w+li[nr][nc], (nr,nc)))
        print("Problem {0}: {1}".format(problem, ans))
if __name__ == '__main__':
    main()