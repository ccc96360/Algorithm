#BOJ1759 암호 만들기 20210313
import sys
from itertools import combinations
input = sys.stdin.readline

def main():
    l,c = map(int,input().rstrip().split())
    li = input().rstrip().split()
    mo = []
    ja = []
    for v in li:
        if v in ['a','e','i','o','u']:
            mo.append(v)
        else: ja.append(v)
    n = len(mo)
    res = set()
    for i in range(1, n+1):
        j = l-i
        if j < 2: break
        for s1 in combinations(mo,i):
            for s2 in combinations(ja,j):
                moja = list(s1+s2)
                moja.sort()
                res.add(''.join(moja))
    res = list(res)
    res.sort()
    for v in res:
        print(v)
if __name__ == '__main__':
    main()