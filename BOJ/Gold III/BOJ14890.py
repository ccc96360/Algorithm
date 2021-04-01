#BOJ14890 경사로 20210401
import sys
input = sys.stdin.readline

def main():
    n,l = map(int,input().rstrip().split())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    res = 2 * n
    for r in range(n):
        skip = 0
        ph = li[r][0]
        cnt = 1
        foots = [False] * n
        for c in range(1,n):
            ch = li[r][c]
            flag = False
            if skip != 0:
                skip -= 1
                ph = ch
                continue
            if ph == ch:
                if not foots[c-1]:
                    cnt += 1
                else:
                    cnt = 1
            elif ch == ph + 1 and cnt >= l and not foots[c-1]:
                cnt = 1
                foots[c-1] = True
            elif ch == ph - 1 and c + l <= n:
                for nc in range(c,c+l):
                    if li[r][nc] != ch and not foots[nc]: 
                        flag = True
                        break
                    else:
                        foots[nc] = True
                skip = l - 1
                cnt = 1
            else:
                flag = True
            if flag:
                res -= 1
                break
            ph = ch

    for c in range(n):
        skip = 0
        ph = li[0][c]
        cnt = 1
        foots = [False] * n
        for r in range(1,n):
            flag = False
            if skip != 0:
                skip -= 1
                continue
            ch = li[r][c]
            if ph == ch:
                if not foots[r-1]:
                    cnt += 1
                else:
                    cnt = 1
            elif ch == ph + 1 and cnt >= l and not foots[r-1]:
                cnt = 1
                foots[r-1] = True
            elif ch == ph - 1 and r + l <= n:
                for nr in range(r,r+l):
                    if li[nr][c] != ch and not foots[nr]: 
                        flag = True
                        break
                    else:
                        foots[nr] = True
                skip = l - 1
                cnt = 1
            else:
                flag = True
            if flag:
                res -= 1
                break
            ph = ch

    print(res)
if __name__ == '__main__':
    main()