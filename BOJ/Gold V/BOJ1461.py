#BOJ1461 도서관 20210510
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split())
    li = sorted(list(map(int,input().rstrip().split())))

    minus = deque()
    plus = deque()
    mx = 0
    flag = False
    for v in li:
        if v < 0:
            minus.append(-v)
            if -v > mx:
                mx = -v
                flag = True
        else:
            plus.appendleft(v)
            if v > mx:
                mx = v
                flag = False

    tmp = minus if flag else plus
    ans = mx
    for _ in range(m):
        if not tmp: break
        tmp.popleft()

    for v in [minus, plus]:
        while v:
            ans += v[0] * 2
            for _ in range(m):
                if not v: break
                v.popleft()
    print(ans)
if __name__ == '__main__':
    main()