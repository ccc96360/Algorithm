#BOJ16434 드래곤 앤 던전 20210527
import sys
from math import ceil
input = sys.stdin.readline

def main():
    n, atk = map(int, input().rstrip().split())
    minHp = curHp = 0
    for _ in range(n):
        t,a,h = map(int, input().rstrip().split())
        if t == 1:
            nOfAtk = ceil(h / atk) - 1
            curHp -= a * nOfAtk
        elif t == 2:
            minHp = min(minHp, curHp)
            curHp += h
            if curHp > 0: curHp = 0
            atk += a
    print(min(minHp, curHp) * -1 + 1)
if __name__ == '__main__':
    main()