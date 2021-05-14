#BOJ9935 문자열 폭발 20210514
import sys
from collections import deque
input = sys.stdin.readline

def main():
    q = deque(input().rstrip())
    bomb = input().rstrip()
    bombSize = len(bomb)
    res = []
    last = deque()
    while q:
        v = q.popleft()
        res.append(v)
        last.append(v)
        if len(last) > bombSize:
            last.popleft()
        #print("현재 문자: {0}, 저장된 문자{1}, 마지막 문자{2}개 {3}".format(v, res, bombSize, last))
        if "".join(last) == bomb:
            for _ in range(bombSize):
                res.pop()
            last = deque()
            for i in res[-bombSize:]:
                last.append(i)
    if res:
        print("".join(res))
    else:
        print("FRULA")
if __name__ == '__main__':
    main()