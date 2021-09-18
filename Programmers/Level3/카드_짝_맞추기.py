from collections import defaultdict, deque
from itertools import permutations
import sys

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def ctrl(r,c, dr, dc, board):
    while True:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < 4 and 0 <= nc < 4):
            return r,c
        else:
            if board[nr][nc] != 0: return nr, nc
            r,c = nr, nc

def bfs(src, dst, board):
    if src == dst: return 0
    visited = set([src])
    q = deque()
    q.append((src,0))
    while q:
        pos, cnt = q.popleft()
        r,c = pos
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if (nr,nc) not in visited:
                    if (nr,nc) == dst: return cnt + 1
                    q.append(((nr,nc), cnt + 1))
                    visited.add((nr,nc))

            nr,nc = ctrl(r,c,dr[i],dc[i],board)
            if (nr, nc) not in visited:
                if (nr,nc) == dst: return cnt + 1
                q.append(((nr,nc), cnt + 1))
                visited.add((nr,nc))
    return 0

def deleteCard(board, l, r):
    board[l[0]][l[1]] = 0
    board[r[0]][r[1]] = 0

def recoverCard(board, l, r, cardNum):
    board[l[0]][l[1]] = cardNum
    board[r[0]][r[1]] = cardNum

mn = sys.maxsize
def move(n, src, order, info, board, idx, cnt):
    global mn
    if n == idx:
        mn = min(mn, cnt)
        return
    cardNum = order[idx]
    l = info[cardNum][0]
    r = info[cardNum][1]

    t = bfs(src, l, board) + bfs(l, r, board)
    deleteCard(board, l, r)
    move(n, r, order, info, board, idx + 1, cnt + t)
    recoverCard(board, l, r, cardNum)

    t = bfs(src, r, board) + bfs(r, l, board)
    deleteCard(board, l, r)
    move(n, l, order, info, board, idx + 1, cnt + t)
    recoverCard(board, l, r, cardNum)

def solution(board, r, c):
    answer = 0
    cursor = (r,c)
    info = defaultdict(list)
    cards = set()
    for i in range(4):
        for j in range(4):
            t = board[i][j]
            if t != 0:
                cards.add(t)
                answer += 1
                info[t].append((i,j))

    n = len(cards)

    for order in permutations(cards, len(cards)):
        r,c = cursor
        move(n, cursor, order, info, board, 0, 0)
    return answer + mn

def main():
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0
    print(solution(board, r, c))
if __name__ == '__main__':
   main()

   




