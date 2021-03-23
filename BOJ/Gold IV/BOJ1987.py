#BOJ20210323 알파벳 20210323 pypy3로 풀림 ㅂㄷㅂㄷ
import sys
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = [False] * 26
li = []
def dfs(p, r, c, res):
    cr,cc = p
    visited[li[cr][cc]] = True
    res += 1
    if res == 26:
        return 26
    curRes = res
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < r and 0 <= nc < c:
            if not visited[li[nr][nc]]:
                res = max(res, dfs((nr,nc), r, c, curRes))
    visited[li[cr][cc]] = False
    return res
def main():
    global li
    r,c = map(int, input().rstrip().split())
    li = [list(map(lambda x : ord(x)-65,input().rstrip())) for _ in range(r)]
    res = dfs((0,0), r, c,0)
    print(res)
if __name__ == '__main__':
    main()