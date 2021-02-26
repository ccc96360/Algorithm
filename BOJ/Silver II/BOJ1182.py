#BOJ1182 부분수열의 합 20210226
import sys
from itertools import combinations
input = sys.stdin.readline

def main():
    n,s = map(int, input().rstrip().split())
    li = list(map(int, input().split()))
    res = 0
    for i in range(1,n+1):
        for v in combinations(li,i):
            if sum(v) == s: res += 1
    print(res)

if __name__ == '__main__':
    main()