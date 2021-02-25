#BOJ6603 로또 20210225
import sys
from itertools import combinations
input = sys.stdin.readline

def main():
    while True:
        li = list(map(int,input().rstrip().split()))
        if li[0] == 0: break
        res = list(combinations(li[1:],6))
        for i in range(int(li[0])):
            res[i] = sorted(list(res[i]))
        res = sorted(res, key = lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
        for v in res: print(*v)
        print()
if __name__ == '__main__':
    main()